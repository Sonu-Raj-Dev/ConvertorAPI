from flask import Flask

app = Flask(__name__)

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

# Your existing '/convert' route
@app.route('/convert', methods=['POST'])
def convert_pdf_to_word_route():
    # Replace with your conversion logic
    return "Conversion endpoint logic goes here."

if __name__ == '__main__':
    app.run(debug=True)
