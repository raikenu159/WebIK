import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session


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
def index():
    """Homepage"""

    return render_template("quiz.html")

@app.route("/quiz", methods=["GET", "POST"]):
def quiz():
    """Take quiz"""
    if request.method == "POST":
        # Run quiz


        #End of quiz sequence (timer = 0):
            # Get final score

            # Add score to database after checking if user achieved top 10 score
            db.execute("INSERT INTO scores (id, username, score, date) VALUES (:sessionid, :username, :score)",

                    score = request.args.get("finalscore"),)



        return redirect("/leaderboard.html")
    else:
        # Create session_id
        # G

        return render_template("quiz.html")


@app.route("/check", methods=["GET"])
def check():

    top10 = db.execute("SELECT TOP 10 * FROM scores ORDERED BY score")

    """Return true if achieved score is in top 10"""

    # Get
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

@app.route("/leaderboard", methods=["GET"]):
def check():
    top10 = db.execute("SELECT TOP 10 * FROM scores ORDERED BY score")
