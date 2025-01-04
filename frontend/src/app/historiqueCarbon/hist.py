import psycopg2
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from urllib.parse import quote_plus
import subprocess  # importer subprocess pour executer des scripts externes

app = FastAPI()  #initialiser l'application FastAPI

#informations de connexion a la base de donnaes PostgreSQL
user = "postgres"  
password = "1234" 
host = "localhost"  
port = "5431"  
database = "carbon_prices"  

#encoder le mot de passe pour eviter les erreurs de cnx (normalement pou les car speciaux)
encoded_password = quote_plus(password)

DATABASE_URL = f"postgresql://{user}:{encoded_password}@{host}:{port}/{database}"

print(DATABASE_URL)  # detection s'il y a un probleme

# Définir un modèle Pydantic pour structurer les données de l'émission de carbone
class CarbonEmissionData(BaseModel):
    date: str 
    price: float  
    change_percent: str  
    price_eth: float  

# fonction pour etablir une connexion a la base de donnees psql
def get_db_connection():
    try:
        conn = psycopg2.connect(DATABASE_URL)  
        return conn  
    except Exception as e:
        print(f"Erreur lors de la connexion à la base de données : {e}")  # afficher l'erreur en cas d'échec
        raise HTTPException(status_code=500, detail="Erreur de connexion à la base de données")  # retourner une erreur HTTP si la connexion echoue

# fonction pour executer un script de scraping, pour endre les prix a jour
def execute_scraping_script():
    try:
        result = subprocess.run(['python', 'scrapp_API.py'], check=True, capture_output=True)  # exécuter le script de scraping
        print("Le fichier de scraping a été exécuté avec succès.")  # afficher un message de succès
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du fichier de scraping : {e}")  # afficher l'erreur en cas d'échec
        raise HTTPException(status_code=500, detail="Erreur d'exécution du script de scraping")  # retourner une erreur HTTP si le script échoue

@app.get("/carbon_emissions", response_model=List[CarbonEmissionData])
def get_carbon_emissions():
    try:
        execute_scraping_script()  #excuter le script de scraping avant de recuperer data
    except:
        print('ok')  
    conn = get_db_connection()  
    cursor = conn.cursor() 
    cursor.execute("SELECT date, price, change_percent, price_eth FROM carbon_emissions_data ORDER BY timestamp ASC")  # exécuter la requete sql ordonnee par timestamp pour les organiser dans visualisation chart
    rows = cursor.fetchall()  
    conn.close()  
    # Retourner les données sous format JSON avec Pydantic
    return [
        CarbonEmissionData(date=row[0], price=row[1], change_percent=row[2], price_eth=row[3])  # transformer chaque ligne en un modèle CarbonEmissionData
        for row in rows  # parcourir toutes les lignes
    ]
