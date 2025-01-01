# Utiliser une image Python officielle
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port (changer selon le microservice)
EXPOSE 8005

# Lancer l'application
<<<<<<< HEAD
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]
=======
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]
>>>>>>> 946826686aaa683e610d177faa214ae6d94a4c96
