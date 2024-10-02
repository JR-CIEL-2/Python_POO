# Utiliser une image Python comme image de base
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le script Python dans le répertoire de travail
COPY main.py .

# Exécuter le script Python
CMD ["python", "main.py"]
