# Utiliser une image de base Python
FROM python:3.9

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt .
COPY app.py /app/

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer les dépendances Python
RUN pip install flask

# Exposer le port sur lequel l'application Flask écoute
EXPOSE 5000

# Définir la commande par défaut pour exécuter l'application  Flask
CMD ["python", "app.py"]

