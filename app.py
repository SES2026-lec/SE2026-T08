from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    print("Hello!")
    print("Alha")
    print("X!")
    return "Hello World! I'm using Flask."
