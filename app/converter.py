# app/converter.py

import os
from flask import send_file
from pdf2docx import Converter

def convert_pdf_to_word(request):
    # Check if the 'pdf' field is part of the request
    if 'pdf' not in request.files:
        return "No file part", 400

    file = request.files['pdf']

    # Ensure the file is a PDF
    if not file.filename.lower().endswith('.pdf'):
        return "Invalid file format. Please upload a PDF.", 400

    # Generate safe file paths
    file_name = file.filename.replace(" ", "_")  # Replace spaces with underscores
    pdf_path = os.path.join(os.getcwd(), file_name)  # Save in the current working directory
    word_path = os.path.join(os.getcwd(), file_name.replace('.pdf', '.docx'))  # .docx file in the same location

    # Save the uploaded PDF
    try:
        file.save(pdf_path)
    except Exception as e:
        return f"Error saving file: {str(e)}", 500

    # Convert PDF to Word using pdf2docx
    try:
        converter = Converter(pdf_path)
        converter.convert(word_path)
        converter.close()
    except Exception as e:
        return f"Error converting PDF to Word: {str(e)}", 500

    # Return the converted Word document
    try:
        return send_file(word_path, as_attachment=True)
    except Exception as e:
        return f"Error sending file: {str(e)}", 500