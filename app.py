from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    print("Hello!")
    print("Alha")
    print("X!")
    print("お茶")
    return "Hello World! I'm using Flask."

# a-2追記