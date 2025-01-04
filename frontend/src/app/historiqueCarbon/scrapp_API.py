import psycopg2
from psycopg2 import sql
from datetime import datetime
import time
import requests
from bs4 import BeautifulSoup
import concurrent.futures  # pour la gestion de l'execution parallele

# url de la page a scraper
url = "https://www.investing.com/commodities/carbon-emissions-historical-data"

# fonction pour obtenir le prix de l'eth (ethereum) en eur pour une date specifique
def get_eth_price_on_date(date):
    try:
        # convertir la date au format iso (jour-mois-annee)
        iso_date = datetime.strptime(date, "%b %d, %Y").strftime("%d-%m-%Y")
        # api de coingecko pour obtenir le prix historique de l'eth
        api_url = f"https://api.coingecko.com/api/v3/coins/ethereum/history?date={iso_date}&localization=false"
        
        response = requests.get(api_url)
        if response.status_code == 200:
            # si la requete reussit, extraire le prix de l'eth
            eth_data = response.json()
            market_data = eth_data.get("market_data", {})
            return market_data.get("current_price", {}).get("eur", None)
        elif response.status_code == 429:
            # si trop de requetes sont envoye, attendre avant de reessayer
            print(f"limite atteinte pour {date}, reessayez plus tard.")
            return None
        else:
            # si la requete echoue, afficher l'erreur
            print(f"erreur http {response.status_code} pour {date}")
            return None
    except Exception as e:
        # en cas d'erreur, afficher le message d'exception
        print(f"erreur lors de la recuperation du prix de l'eth pour {date}: {e}")
        return None

# connexion a la base de donnees postgresql
conn = psycopg2.connect(
    dbname="carbon_prices",
    user="postgres",
    password="1234",
    host="localhost",  
    port="5431"
)
cursor = conn.cursor()

# creer la table dans la base de donnees si elle n'existe pas deja
cursor.execute("""
    CREATE TABLE IF NOT EXISTS carbon_emissions_data (
        date VARCHAR(50) PRIMARY KEY,
        price DOUBLE PRECISION,
        change_percent VARCHAR(50),
        price_eth DOUBLE PRECISION,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")
conn.commit()  # appliquer la commande sql pour creer la table

# envoyer une requete get pour recuperer la page de donnees
response = requests.get(url)

if response.status_code == 200:     # si la requete est reussie, analyser le contenu html de la page, 200=ok
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='freeze-column-w-1')
    rows = table.find_all('tr')[1:]  # ignorer l'en-tete de la table
    last_eth_price = None  # dernier prix eth connu pour eviter les valeurs manquantes

    def process_row(row, last_eth_price):
        cols = row.find_all('td')  
        date = cols[0].text.strip() 
        price = float(cols[1].text.strip().replace(',', '.'))  
        change_percent = cols[6].text.strip()  

        #obtenir le prix de l'eth pour la date en question
        eth_price = get_eth_price_on_date(date) or last_eth_price

        return (date, price, change_percent, eth_price)

    # utiliser threadpoolexecutor pour executer plusieurs appels api en parallele
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # soumettre chaque ligne du tableau pour traitement parallele
        future_to_row = {executor.submit(process_row, row, last_eth_price): row for row in rows}

        for future in concurrent.futures.as_completed(future_to_row):
            row = future_to_row[future]  
            try:
                # extraire les resultats du traitement de chaque ligne
                date, price, change_percent, eth_price = future.result()

                # verifier si les donnees existent deja dans la base de donnees
                cursor.execute("SELECT 1 FROM carbon_emissions_data WHERE date = %s", (date,))
                if cursor.fetchone():
                    print(f"donnees deja presentes pour la date {date}. Ignore.")
                else:
                    # inserer les data dans la base de donnees
                    cursor.execute("""
                        INSERT INTO carbon_emissions_data (date, price, change_percent, price_eth, timestamp)
                        VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP)
                    """, (date, price, change_percent, price / eth_price))  # calculer le prix de l'emission en eth
                    conn.commit()  # valider l'insertion dans la base de donnees

            except Exception as e:
                print(f"erreur lors du traitement de la ligne : {e}")  # gerer les erreurs

    print("donnees inserees dans la base de donnees.")  #afficher message de succes
else:
    print("erreur lors de la recuperation de la page")  # afficher un message d'erreur si la page n'a pas ete recupee correctement

cursor.close()
conn.close()
