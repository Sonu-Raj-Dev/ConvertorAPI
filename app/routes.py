from app import app
from flask import request, send_file
from app.converter import convert_pdf_to_word

@app.route('/convert', methods=['POST'])
def convert_pdf_to_word_route():
    return convert_pdf_to_word(request)

