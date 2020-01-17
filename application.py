import os
import requests

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from datetime import datetime



# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///triviasite.db")

@app.route("/")
def homepage():
    """Homepage"""
    # deze functie laadt alleen de homepage
    return render_template("index.html")



@app.route("/startquiz", methods=["GET","POST"])
def startquiz():
    """Explain quiz and start"""
    return render_template("startquiz.html")



@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Take quiz"""

    if request.method == "POST":
        print("POST request")
    #     # nadat de check functie is uitgevoerd worden de username(als de gebruiker in de top 10 zit) en de score gesubmit
    #     # deze functie voegt deze dan toe aan de database zodat deze op de leaderboard weergegeven kunnen worden
    #     id = session["user_id"]
    #     username = request.form.get('username')
    #     scoreTotaal = request.form.get('scoreTotaal')
    #     # ook voegen de de score per catagorie toe om de gebruiker inzicht te gevenen in zijn prestaties per catagorie
    #     score1 = request.form.get('score1')
    #     score2 = request.form.get('score2')
    #     # etc. (catagorieen nog te bepalen)
    #     db.execute("INSERT INTO scores (id, username, scoreTotaal, score1, score2, etc., date) VALUES (:sessionid, :username, :score)",
    #         id = id,
    #         username = username,
    #         scoreTotaal = scoreTotaal,
    #         score1 = score1,
    #         score2 = score2,
    #         etc)
    #     return render_template("leaderboard.html")

    # else:
        # voordat de quiz begint word er een row binnen de database met daarin een user id aangemaakt voor de gebruiker
        # daarna word een request gestuurd naar de api voor de vragen die in de quiz moeten komen (50 per categorie, 5 categorieen)
        # dan worden de vragen om en om gesorteerd zodat de gebruiker ongeveer hetzelfde aantal vragen uit elke catagorie krijgt
    else:
        db.execute("INSERT INTO scores (score) VALUES (0)")
        return render_template("quiz.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if achieved score is in top 10"""
    # voordat de quiz.html de score submit checken we of de gebruiker in de top 10 van gebruikers zit
    # we returnen dan True/False naar de quiz.html, deze zal de gebruiker om een naam vragen als hij
    # in de top 10 zit zodat we die kunnen laten zien op de leaderboard en anders een pop up geven dat de quiz voorbij is
    top10 = db.execute("SELECT TOP 10 * FROM scores ORDERED BY score")

    username = request.args.get("username")

    # Set result to false if username is one character or less
    if len(username) <= 1:
        return jsonify(False)

    # Check if username is in use
    usernameFound = db.execute("SELECT * FROM users WHERE username = :username",
                        username = username)
    if usernameFound:
        return jsonify(False)

    return jsonify(True)

@app.route("/leaderboard")
def leaderboard():
    """Display the current leaderboard and some statistics about the users performance"""
    # hier halen we de data op uit de database, die we nodig hebben om de leaderboard en de statistieken te laten zien
    # top10 = db.execute("SELECT TOP 10 username, scoreTotaal FROM scores ORDERED BY score")
    # userdata = db.execute('SELECT * FROM scores WHERE id = :id')
    # deze geven we mee wanneer we de leaderboard pagina renderen

    scores = db.execute("SELECT * FROM scores")
    # session["user_id"] = scores[0]["id"]
    # print(session["user_id"])

    return render_template("leaderboard.html", scores=scores)#, top10, userdata)

@app.route("/barchart")
def barchart():
    """Display in a barchart the score per category"""



    return render_template("barchart.html")


