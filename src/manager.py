from flask import Flask, render_template, redirect, request, abort
from .logic.conjugate import getVerbData

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/connect", methods=["POST"])
def connect():
    if request.method == "POST":
        verb = request.form["userVerb"]
        return redirect(f"/{verb}")

@app.route("/<verb>")
def dataPage(verb):
    verbData, verbTranslation = getVerbData(verb)
    if verbData and verbTranslation:
        return render_template("table.html", verbData=verbData, verbTranslation=verbTranslation)
    return abort(404)