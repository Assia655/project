# Étape 1 : Construction
FROM node:18 AS build-stage

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier package.json et package-lock.json pour installer les dépendances
COPY package.json package-lock.json ./

# Installer les dépendances
RUN npm install

# Copier tout le code source dans le conteneur
COPY . .

# Construire l'application Angular pour la production
RUN npm run build -- --configuration production

# Étape 2 : Serveur Nginx
FROM nginx:alpine AS production-stage

# Copier le build Angular dans le dossier nginx/html
COPY --from=build-stage /app/dist/frontend2 /usr/share/nginx/html

# Copier le fichier de configuration Nginx personnalisé (si nécessaire)
COPY nginx.conf /etc/nginx/nginx.conf

# Exposer le port 80 pour servir l'application
EXPOSE 80

# Commande pour démarrer Nginx
CMD ["nginx", "-g", "daemon off;"]
