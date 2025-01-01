<<<<<<< HEAD
=======
# Étape 1 : Construire l'environnement à partir d'une image Python légère
>>>>>>> 946826686aaa683e610d177faa214ae6d94a4c96
FROM python:3.10-slim AS base

# Définir le répertoire de travail à l'intérieur du conteneur
WORKDIR /app

# Copier le fichier requirements.txt contenant les dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le contenu de l'application dans le conteneur
COPY . .

# Exposer le port utilisé par l'application FastAPI
EXPOSE 8002

# Définir la commande de démarrage pour Uvicorn
<<<<<<< HEAD
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]
=======
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8002"]
>>>>>>> 946826686aaa683e610d177faa214ae6d94a4c96
