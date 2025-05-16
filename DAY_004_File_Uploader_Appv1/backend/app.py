from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import io
import base64
import qrcode
from werkzeug.utils import secure_filename
from ai.analyzer import analyze_file  # Ensure this exists and works

UPLOAD_FOLDER = 'uploads'
FRONTEND_FOLDER = '../frontend'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__, static_folder=FRONTEND_FOLDER, static_url_path='')
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No selected file'}), 400

    if not allowed_file(file.filename):
        return jsonify({'success': False, 'error': 'Invalid file type'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    try:
        # AI analysis
        ai_result = analyze_file(filepath)

        # QR Code generation
        download_url = f"http://localhost:5000/files/{filename}"
        qr = qrcode.make(download_url)
        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")
        qr_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

        return jsonify({
            'success': True,
            'filename': filename,
            'ai_analysis': ai_result,
            'download_url': download_url,
            'qr_code_base64': qr_base64
        })

    except Exception as e:
        return jsonify({'success': False, 'error': f'Processing error: {str(e)}'}), 500

@app.route('/files/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
