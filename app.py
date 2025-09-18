# naredimo strežnik
from flask import Flask, render_template
# pip install flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcLove")
def calc():
    print("sem tukaj")
    return render_template("index.html")

app.run(debug = True)
