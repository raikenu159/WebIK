import os
import uuid

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
        return render_template("quiz.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if achieved score is in top 10"""
    # voordat de quiz.html de score submit checken we of de gebruiker in de top 10 van gebruikers zit
    # we returnen dan True/False naar de quiz.html, deze zal de gebruiker om een naam vragen als hij
    # in de top 10 zit zodat we die kunnen laten zien op de leaderboard en anders een pop up geven dat de quiz voorbij is
    userScore = int(request.args.get("score"))
    db.execute('INSERT INTO scores (score) VALUES (:score)', score=userScore)
    print(userScore)
    leaderboard= db.execute('SELECT score FROM scores')
    print(leaderboard)

    ranking = 0
    for score in leaderboard:
        if userScore <= score['score']:
            ranking+= 1

    percentile = ((1-(ranking / len(leaderboard))) * 100)

    if ranking < 10:
        return jsonify('Congratulations! you are number ' + str(ranking) + ' on the leaderboard.')
    elif percentile > 50:
        return jsonify('Well done you scored bettter than {0:.2f}% of previous users!'.format(percentile))
    elif percentile >= 25:
        return jsonify('You scored bettter than {0:.2f}% of previous users.'.format(percentile))
    elif percentile < 25:
        return jsonify('Better luck next time, you scored in the bottom quartile.')

@app.route("/leaderboard")
def leaderboard():
    """Display the current leaderboard and some statistics about the users performance"""

    #session["user_id"] = str(uuid.uuid4())
    topscores = db.execute("SELECT * FROM scores ORDER BY score")[::-1][:10]

    return render_template("leaderboard.html", scores=topscores)

@app.route("/barchart")
def barchart():
    """Display in a barchart the score per category"""

    return render_template("barchart.html")

<<<<<<< HEAD
=======
@app.route("/load_questions", methods=["GET"])
def load_questions():
    """fetches questions"""
    a = requests.get("https://opentdb.com/api.php?amount=5&category=9").json()['results'] # general knowledge
    b = requests.get("https://opentdb.com/api.php?amount=5&category=18").json()['results'] # computer science
    c = requests.get("https://opentdb.com/api.php?amount=5&category=22").json()['results'] # geopraphy
    d = requests.get("https://opentdb.com/api.php?amount=5&category=23").json()['results'] # history
    e = requests.get("https://opentdb.com/api.php?amount=5&category=27").json()['results'] # animals

    questions = []
    for i in range(5):
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
        random.shuffle(answers)

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
>>>>>>> ce6120282382a3b4705047b83a0972c54e0debbf

