# app/app.py

from flask import Flask, request, send_file
from flask_cors import CORS  # Import CORS
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Root route for homepage
@app.route('/')
def home():
    return """
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1>Welcome to the PDF to Word Converter API!</h1>
            <p>The API is live and running successfully.</p>
            <p>Use the <code>/convert</code> endpoint to convert your PDF files to Word documents.</p>
        </body>
    </html>
    """

# Convert route to handle POST requests
@app.route('/convert', methods=['POST'])
def convert_pdf_to_word_route():
    from app.converter import convert_pdf_to_word  # Import here to avoid circular import
    return convert_pdf_to_word(request)

if __name__ == '__main__':
    app.run(debug=True)