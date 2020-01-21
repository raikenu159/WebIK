import os
import uuid
import requests
import random
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from datetime import datetime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

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
        name = request.form.get("username")
        db.execute("UPDATE scores SET username = :name WHERE id = :id", name=name, id=session["user_id"])
        topscores = db.execute("SELECT * FROM scores ORDER BY score")[::-1][:10]
        return render_template("leaderboard.html", scores=topscores, played="Play Again!")
    else:
        return render_template("quiz.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if achieved score is in top 10"""
    # voordat de quiz.html de score submit checken we of de gebruiker in de top 10 van gebruikers zit
    # we returnen dan True/False naar de quiz.html, deze zal de gebruiker om een naam vragen als hij
    # in de top 10 zit zodat we die kunnen laten zien op de leaderboard en anders een pop up geven dat de quiz voorbij is
    userScore = int(request.args.get("score"))
    row = db.execute('INSERT INTO scores (score) VALUES (:score)', score=userScore)
    session["user_id"] = row

    leaderboard= db.execute('SELECT score FROM scores')

    ranking = 0
    for score in leaderboard:
        if userScore <= score['score']:
            ranking+= 1

    percentile = ((1-(ranking / len(leaderboard))) * 100)
    if ranking < 10:
        return jsonify(['Congratulations! you are number ' + str(ranking) + ' on the leaderboard.', True])
    elif percentile > 50:
        return jsonify('Well done you scored better than {0:.2f}% of previous users!'.format(percentile))
    elif percentile >= 25:
        return jsonify('You scored better than {0:.2f}% of previous users.'.format(percentile))
    elif percentile < 25:
        return jsonify('Better luck next time, you scored in the bottom quartile.')

@app.route("/leaderboard")
def leaderboard():
    """Display the current leaderboard and some statistics about the users performance"""

    topscores = db.execute("SELECT * FROM scores ORDER BY score")[::-1][:10]

    return render_template("leaderboard.html", scores=topscores, played="Play Now!")

@app.route("/barchart")
def barchart():
    """Display in a barchart the score per category"""

    return render_template("barchart.html")

@app.route("/load_questions", methods=["GET"])
def load_questions():
    """fetches questions"""
    a = requests.get("https://opentdb.com/api.php?amount=50&category=9").json()['results'] # general knowledge
    b = requests.get("https://opentdb.com/api.php?amount=50&category=18").json()['results'] # computer science
    c = requests.get("https://opentdb.com/api.php?amount=50&category=22").json()['results'] # geopraphy
    d = requests.get("https://opentdb.com/api.php?amount=50&category=23").json()['results'] # history
    e = requests.get("https://opentdb.com/api.php?amount=50&category=27").json()['results'] # animals

    questions = []
    for i in range(50):
        questions.append(a[i])
        questions.append(b[i])
        questions.append(c[i])
        questions.append(d[i])
        questions.append(e[i])

    questions_js = []
    correct_answers = []
    for question in questions:
        answers = question['incorrect_answers']
        answers.append(question['correct_answer'])
        if len(answers) > 2:
            random.shuffle(answers)
        else:
            answers = ['True', 'False']

        questions_js.append({
            'answers' : answers,
            'question' : question['question'],
            'difficulty' : question['difficulty'],
            'category' : question['category'],
            'type' : question['type'],
        })

        correct_answers.append(question['correct_answer'])

    session['correct_answers'] = correct_answers

    return jsonify(questions_js)


@app.route("/check_answer")
def check_answer():
    answer = request.args.get('answer');
    correct_answer = session['correct_answers'][0]
    session['correct_answers'].remove(session['correct_answers'][0])
    if answer == correct_answer:

        return jsonify(True)
    else:

        return jsonify(False)

