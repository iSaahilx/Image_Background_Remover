from flask import Flask, render_template, request, jsonify, send_file
from rembg import remove
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file:
            input_img = Image.open(file.stream)
            output_img = remove(input_img, post_process_mask=True)
            img_io = BytesIO()
            output_img.save(img_io, 'PNG')
            img_io.seek(0)

            return send_file(img_io, mimetype='image/png',as_attachment=True, download_name='meow.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)