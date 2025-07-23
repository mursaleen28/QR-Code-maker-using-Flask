from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_qr():
    data = request.form['qrdata']
    if not data:
        return "No data provided", 400

    # Generate QR code
    img = qrcode.make(data)

    # Save to memory
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    return send_file(buffer, mimetype='image/png', as_attachment=True, download_name='qr_code.png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

           