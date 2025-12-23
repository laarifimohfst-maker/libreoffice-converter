# LibreOffice File Converter

Un convertisseur de fichiers utilisant LibreOffice dans un conteneur Docker avec interface web Flask.

## 🚀 Fonctionnalités
- Conversion de fichiers (DOCX, TXT, ODT, etc.) vers PDF, DOCX, etc.
- Interface web simple
- Utilisation de LibreOffice en ligne de commande
- Conteneur Docker pour isolation
# 🏗️ Architecture du Projet

## 📁 Structure des Fichiers

```
libreoffice-converter/
│
├── 📂 app/                          # Application principale
│   ├── 📄 app.py                    # ⚙️ BACKEND (Flask)
│   │   ├── Routes API
│   │   ├── Validation
│   │   ├── Conversion LibreOffice
│   │   └── Gestion fichiers
│   │
│   └── 📂 templates/
│       └── 📄 index.html            # 🎨 FRONTEND
│           ├── HTML (Structure)
│           ├── CSS (Styles)
│           └── JavaScript (Logique)
│
├── 📂 uploads/                      # Fichiers uploadés
├── 📂 downloads/                    # Fichiers convertis
│
├── 📄 Dockerfile                    # Image Docker
├── 📄 docker-compose.yml            # Configuration Docker
├── 📄 requirements.txt              # Dépendances Python
└── 📄 README.md                     # Documentation
```

## 🎯 Architecture en 2 Parties

### 1️⃣ FRONTEND
**Fichier :** `app/templates/index.html`
- Interface utilisateur
- HTML + CSS + JavaScript
- Communication avec backend

### 2️⃣ BACKEND
**Fichier :** `app/app.py`
- Flask (framework web)
- Routes API
- Conversion LibreOffice
- Gestion fichiers

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
