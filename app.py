from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "I want go Home, D'oh!!"
