from flask import Flask, render_template, request, send_file, jsonify
import os
import subprocess
import uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configuration
app.config['UPLOAD_FOLDER'] = '/app/uploads'
app.config['DOWNLOAD_FOLDER'] = '/app/downloads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
ALLOWED_EXTENSIONS = {
    'doc', 'docx', 'odt', 'txt', 'rtf',  # Documents
    'xls', 'xlsx', 'ods', 'csv',         # Tableurs
    'ppt', 'pptx', 'odp',                # Présentations
    'pdf', 'jpg', 'png', 'bmp'          # Autres
}

def allowed_file(filename):
    """Vérifier si le fichier a une extension autorisée"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_file(input_path, output_format):
    """Convertir un fichier avec LibreOffice"""
    # Générer un nom de fichier unique pour le résultat
    unique_id = str(uuid.uuid4())[:8]
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_filename = f"{base_name}_{unique_id}.{output_format}"
    output_path = os.path.join(app.config['DOWNLOAD_FOLDER'], output_filename)
    
    # Construire la commande LibreOffice
    command = [
        'libreoffice',
        '--headless',          # Pas d'interface graphique
        '--convert-to', output_format,
        '--outdir', app.config['DOWNLOAD_FOLDER'],
        input_path
    ]
    
    try:
        # Exécuter la conversion
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=30  # Timeout après 30 secondes
        )
        
        if result.returncode == 0:
            # Le fichier converti aura le nom original + nouvelle extension
            # On le renomme pour éviter les conflits
            expected_output = os.path.splitext(os.path.basename(input_path))[0] + f".{output_format}"
            expected_path = os.path.join(app.config['DOWNLOAD_FOLDER'], expected_output)
            
            if os.path.exists(expected_path):
                os.rename(expected_path, output_path)
                return output_path
            else:
                return None
        else:
            print(f"Erreur LibreOffice: {result.stderr}")
            return None
            
    except subprocess.TimeoutExpired:
        print("Timeout lors de la conversion")
        return None
    except Exception as e:
        print(f"Erreur: {e}")
        return None

@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Traiter l'upload de fichier"""
    # Vérifier si un fichier a été envoyé
    if 'file' not in request.files:
        return jsonify({'error': 'Aucun fichier sélectionné'}), 400
    
    file = request.files['file']
    
    # Vérifier si un fichier a été sélectionné
    if file.filename == '':
        return jsonify({'error': 'Aucun fichier sélectionné'}), 400
    
    # Vérifier l'extension du fichier
    if not allowed_file(file.filename):
        return jsonify({'error': 'Type de fichier non supporté'}), 400
    
    # Récupérer le format cible
    target_format = request.form.get('format', 'pdf')
    
    # Sécuriser le nom du fichier
    filename = secure_filename(file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Sauvegarder le fichier uploadé
    file.save(input_path)
    
    # Convertir le fichier
    output_path = convert_file(input_path, target_format)
    
    if output_path and os.path.exists(output_path):
        # Retourner le fichier converti
        return send_file(
            output_path,
            as_attachment=True,
            download_name=os.path.basename(output_path)
        )
    else:
        return jsonify({'error': 'Échec de la conversion'}), 500

@app.route('/formats')
def get_formats():
    """Retourner les formats supportés"""
    formats = {
        'pdf': 'PDF Document',
        'docx': 'Microsoft Word',
        'odt': 'OpenDocument Text',
        'txt': 'Plain Text',
        'html': 'HTML Document',
        'jpg': 'JPEG Image',
        'png': 'PNG Image',
        'xlsx': 'Microsoft Excel',
        'ods': 'OpenDocument Spreadsheet',
        'pptx': 'Microsoft PowerPoint'
    }
    return jsonify(formats)

if __name__ == '__main__':
    # Créer les dossiers s'ils n'existent pas
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['DOWNLOAD_FOLDER'], exist_ok=True)
    
    # Démarrer l'application
    app.run(host='0.0.0.0', port=5000, debug=True)
