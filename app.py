# app.py
import os
import logging
from flask import Flask, render_template, request, jsonify, send_file
from rembg import remove
from PIL import Image, UnidentifiedImageError
from io import BytesIO
from flask_cors import CORS

# Basic config
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder="templates", static_folder="static")
CORS(app)  # remove this line if you don't need cross-origin access

# Limit upload size (e.g., 10 MB)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10 MB

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp', 'bmp', 'tiff'}


def allowed_filename(filename: str) -> bool:
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if not allowed_filename(file.filename):
            return jsonify({'error': 'Unsupported file type'}), 400

        try:
            # Ensure a consistent mode for rembg
            input_img = Image.open(file.stream).convert("RGBA")
        except UnidentifiedImageError:
            logger.exception("Uploaded file is not a valid image")
            return jsonify({'error': 'Invalid image file'}), 400
        except Exception:
            logger.exception("Failed to open uploaded image")
            return jsonify({'error': 'Failed to process image'}), 500

        try:
            output_img = remove(input_img, post_process_mask=True)
            img_io = BytesIO()
            output_img.save(img_io, format='PNG')
            img_io.seek(0)

            # send file as attachment
            return send_file(
                img_io,
                mimetype='image/png',
                as_attachment=True,
                download_name='meow.png'
            )
        except Exception:
            logger.exception("Error during background removal")
            return jsonify({'error': 'Background removal failed'}), 500

    # GET
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    # Use FLASK_DEBUG=1 to enable debug in development only
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    # Note: In production on Render you should use gunicorn:
    #   Start command: gunicorn app:app --bind 0.0.0.0:$PORT
    app.run(host='0.0.0.0', port=port, debug=debug)
