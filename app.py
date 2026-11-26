from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    print("Hello!")
    print("Alha")
    print("X!")
    print("お茶")
    print("牛乳")
    print("コーヒー")
    print("ほうじ茶")
    return "Hello World! I'm using Flask."

# 課題5追記