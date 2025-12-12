# LibreOffice File Converter

Un convertisseur de fichiers utilisant LibreOffice dans un conteneur Docker avec interface web Flask.

## 🚀 Fonctionnalités
- Conversion de fichiers (DOCX, TXT, ODT, etc.) vers PDF, DOCX, etc.
- Interface web simple
- Utilisation de LibreOffice en ligne de commande
- Conteneur Docker pour isolation

## 📋 Formats supportés
- **Entrée** : .docx, .doc, .odt, .txt, .rtf, .html, .xlsx, .xls
- **Sortie** : .pdf, .docx, .txt, .odt, .html, .jpg, .png

## 🛠 Installation

### Prérequis
- Docker
- Docker Compose

### Installation
```bash
git clone https://github.com/VOTRE_NOM/libreoffice-converter.git
cd libreoffice-converter
docker-compose up --build~
