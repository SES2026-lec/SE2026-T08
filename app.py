from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    print("Hello!")
    print("Alha")
    return "Hello World! I'm using Flask."
