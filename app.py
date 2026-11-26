from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    print("Hello!")
    return "Hello World! I'm using Flask."
