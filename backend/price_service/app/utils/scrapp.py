import psycopg2
from psycopg2 import sql
from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
import concurrent.futures  # pour la gestion de l'execution parallele

# url de la page a scraper
url = "https://www.investing.com/commodities/carbon-emissions-historical-data"

# fonction pour obtenir le prix de carbon en eth et en eur pour une date specifique
def get_eth_price_on_date(date):
    try:
        iso_date = datetime.strptime(date, "%b %d, %Y").strftime("%d-%m-%Y")
        # api de coingecko pour obtenir le prix historique de l'eth
        api_url = f"https://api.coingecko.com/api/v3/coins/ethereum/history?date={iso_date}&localization=false"
        
        response = requests.get(api_url)
        if response.status_code == 200:
            eth_data = response.json()
            market_data = eth_data.get("market_data", {})
            return market_data.get("current_price", {}).get("eur", None)
        elif response.status_code == 429:
            # print(f"limite atteinte pour {date}, reessayez plus tard.")
            return None
        else:
            # print(f"erreur http {response.status_code} pour {date}")
            return None
    except Exception as e:
        # print(f"erreur lors de la recuperation du prix de l'eth pour {date}: {e}")
        return None

def process_row(row, last_eth_price):
    cols = row.find_all('td')  
    date = cols[0].text.strip() 
    price = float(cols[1].text.strip().replace(',', '.'))  
    change_percent = cols[6].text.strip()  

    eth_price = get_eth_price_on_date(date) or last_eth_price

    return (date, price, change_percent, eth_price)

def process_data_backwards(conn, cursor, rows, last_eth_price):
    for row in reversed(rows):
        cols = row.find_all('td')
        date = cols[0].text.strip()

        # Vérifier si la date existe dans la base de données
        cursor.execute("SELECT 1 FROM carbon_emissions_data WHERE date = %s", (date,))
        if cursor.fetchone():  # Si la date existe, stopper l'insertion
            print(f"Donnees deja presentes pour la date {date}. Arret du scrapping.")
            break

        try:
            price = float(cols[1].text.strip().replace(',', '.'))
            change_percent = cols[6].text.strip()

            eth_price = get_eth_price_on_date(date) or last_eth_price
            if eth_price is None or eth_price == 0:
                print(f"ETH price is invalid for date {date}. Skipping insertion.")
                continue

            # Insérer les données dans la base de données
            cursor.execute(""" 
                INSERT INTO carbon_emissions_data (date, price, change_percent, price_eth, timestamp)
                VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
            """, (date, price, change_percent, price / eth_price))
            conn.commit()

            last_eth_price = eth_price  # Mettre à jour le dernier prix ETH

        except Exception as e:
            print(f"Erreur lors du traitement de la ligne pour la date {date} : {e}")


def scrape_and_insert_data():
    conn = psycopg2.connect(
        dbname="carbon_prices",
        dbname="carbon_prices",
        user="postgres",
        password="1234",
        host="price_service_db",
        port="5432"
    )
    cursor = conn.cursor()

    # Créer la table dans la base de données si elle n'existe pas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carbon_emissions_data (
            date VARCHAR(50) PRIMARY KEY,
            price DOUBLE PRECISION,
            change_percent VARCHAR(50),
            price_eth DOUBLE PRECISION,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()

    # Envoyer une requête GET pour récupérer la page de données
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find('table', class_='freeze-column-w-1')
        rows = table.find_all('tr')[1:]  # Ignorer l'en-tête de la table
        last_eth_price = None

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_row = {executor.submit(process_row, row, last_eth_price): row for row in rows}

            for future in concurrent.futures.as_completed(future_to_row):
                row = future_to_row[future]
                try:
                    date, price, change_percent, eth_price = future.result()

                    # Vérifier si les données existent déjà
                    cursor.execute("SELECT 1 FROM carbon_emissions_data WHERE date = %s", (date,))
                    if cursor.fetchone():
                        print(f"Données déjà présentes pour la date {date}. Ignorées.")
                        continue

                    if eth_price is None or eth_price == 0:
                        print(f"ETH price is invalid for date {date}. Skipping insertion.")
                        continue

                    # Insérer les données dans la base de données
                    cursor.execute("""
                        INSERT INTO carbon_emissions_data (date, price, change_percent, price_eth, timestamp)
                        VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
                    """, (date, price, change_percent, price / eth_price))
                    conn.commit()

                except Exception as e:
                    print(f"Erreur lors du traitement de la ligne pour la date {date} : {e}")

        print("Données insérées dans la base de données.")

        # Traiter les données en arrière (commencer par la fin du tableau)
        process_data_backwards(conn, cursor, rows, last_eth_price)

    else:
        print(f"Erreur lors de la récupération de la page. Code HTTP: {response.status_code}")

    cursor.close()
    conn.close()


scrape_and_insert_data()
