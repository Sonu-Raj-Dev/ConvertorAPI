from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/')
def home():
    return """
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center; margin-top: 50px;">
            <h1>API is running successfully!</h1>
            <p>Access the conversion endpoint at <a href="/convert">/convert</a>.</p>
        </body>
    </html>
    """

# Your existing '/convert' route goes here...

if __name__ == '__main__':
    app.run(debug=True)
