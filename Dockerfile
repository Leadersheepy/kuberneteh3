# Utiliser une image de base Python
FROM python:3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier le reste des fichiers dans le conteneur
COPY app.py .

# Exposer le port sur lequel l'application Flask écoute
EXPOSE 5000

# Définir la commande par défaut pour exécuter l'application  Flask
CMD ["python", "app.py"]
