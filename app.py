from app import app
from flask import request, send_file
from app.converter import convert_pdf_to_word

@app.route('/convert', methods=['POST'])
def convert_pdf_to_word_route():
    return convert_pdf_to_word(request)

if __name__ == '__main__':
    print("Starting the PDF to Word conversion API...")
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
