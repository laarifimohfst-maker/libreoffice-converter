# Utiliser une image Python avec système complet
FROM python:3.9-slim-bullseye

# Installer LibreOffice
RUN apt-get update && \
    apt-get install -y \
    libreoffice \
    libreoffice-writer \
    fonts-dejavu \
    && apt-get clean

# Installer Flask
RUN pip install flask

# Configuration
ENV HOME=/tmp
RUN mkdir -p /app/uploads /app/downloads
RUN chmod 777 /app/uploads /app/downloads

WORKDIR /app
COPY ./app /app

EXPOSE 5000
CMD ["python", "app.py"]
