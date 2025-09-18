# naredimo strežnik
from flask import Flask, render_template, request
import random
# pip install flask
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calcLove")
def calc():
    req = request.args
    # če pride tvoje ime v input
    # vrni 100%
    ime1 = req.get("ime1")
    ime2 = req.get("ime2")
    rnd = random.randint(0,100)
    rez = f"{ime1} + {ime2} = {rnd}%"
    return render_template("index.html", rezultat = rez)

app.run(debug = True)
