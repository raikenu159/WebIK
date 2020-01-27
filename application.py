import os
import uuid
import requests
import random
import json
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
db = SQL("sqlite:///trivia.db")



@app.route("/")
def homepage():
    """Homepage"""
    # deze functie laadt alleen de homepage
    session.clear()

    # create table scores in database
    db.execute("CREATE TABLE if not exists 'scores' ('position' integer, 'id' integer NOT NULL PRIMARY KEY, 'username' varchar(16), 'score' integer, 'date' DATE DEFAULT CURRENT_DATE)")

    # return de index.html template
    return render_template("index.html")



@app.route("/startquiz", methods=["GET","POST"])
def startquiz():
    """Explain quiz and start"""

    # return de startquiz template
    return render_template("startquiz.html")



@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Take quiz"""

    # user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # get username from html form
        name = request.form.get("username")

        # insert username into DB
        db.execute("UPDATE scores SET username = :name WHERE id = :id", name=name, id=session["user_id"])
        topscores = db.execute("SELECT * FROM scores ORDER BY score")[::-1][:10]

        # render current leaderboard after quiz with new user added in
        return render_template("leaderboard.html", scores=topscores, played='Try again!')


    # if request method == GET create session with user_id & define all scores as 0

    else:

        # if no username given as input score equals 0
        row = db.execute('INSERT INTO scores (score) VALUES (0)')
        session["user_id"] = row
        session["category_scores"] = {
        'General Knowledge' : 0,
        'Computer Science' : 0,
        'Geography' : 0,
        'History' : 0,
        'Animals' : 0
        }
        session["difficulty_scores"] = {
        'easy' : 0,
        'medium' : 0,
        'hard' : 0
        }
        session["type_scores"] = {
        'boolean' : 0,
        'multiple' : 0
        }
        session['question_results'] = []
        # return de quiz.html template
        return render_template("quiz.html")



@app.route("/check", methods=["GET"])
def check():
    """Return true if achieved score is in top 10"""
    # voordat de quiz.html de score submit checken we of de gebruiker in de top 10 van gebruikers zit
    # we returnen dan True/False naar de quiz.html, deze zal de gebruiker om een naam vragen als hij
    # in de top 10 zit zodat we die kunnen laten zien op de leaderboard en anders een pop up geven dat de quiz voorbij is

    # get user score from frontend and update into DB
    userScore = int(request.args.get("score"))
    db.execute('UPDATE scores SET score=:score WHERE id = :id', score=userScore, id=session["user_id"])

    leaderboard= db.execute('SELECT score FROM scores')

    # check position in current leadeboard
    ranking = 0
    for score in leaderboard:
        if userScore <= score['score']:
            ranking+= 1

    # calculate and return in which quartile user scored
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

    # select the top 10 scores from the scores database
    position = [i for i in range(1,11)]
    topscores = db.execute("SELECT * FROM scores ORDER BY score")[::-1][:10]

    # check if the user has already played the quiz: if not display button 'play now'
    try:
        session['user_id']
    except:
        return render_template("leaderboard.html", scores=topscores, played='Play now!', position=position)

    # if the user has played the quiz but did not make the topscores display 'try again'
    return render_template("leaderboard.html", scores=topscores, played='Try again!', position=position)


@app.route("/delete_username")
def delete_username():
    """Delete the username of the user from the leaderboards"""

    # delete the score from the database
    db.execute("DELETE FROM scores WHERE id=:id", id=session["user_id"])

    # redirect to homepage
    return redirect("/")



@app.route("/barchart")
def barchart():
    """Display in a barchart the score per category"""

    # add all scores per categroy from current user's session
    category = []
    category.append([score for score in session['category_scores'].values()])
    category.append([name for name in session['category_scores'].keys()])
    category.append('Category scores')

    difficulty = []
    difficulty.append([score for score in session['difficulty_scores'].values()])
    difficulty.append([name for name in session['difficulty_scores'].keys()])
    difficulty.append('Difficulty scores')

    types = []
    types.append([score for score in session['type_scores'].values()])
    types.append([name for name in session['type_scores'].keys()])
    types.append('Type scores')


    values = [category, difficulty, types]
    # render barchart html page with values
    session['chart_data'] = values
    return render_template("barchart.html")



@app.route("/load_questions", methods=["GET"])
def load_questions():
    """fetches questions"""

    # request questions from API per category:
    # general knowledge
    a = requests.get("https://opentdb.com/api.php?amount=50&category=9").json()['results']
    # computer science
    b = requests.get("https://opentdb.com/api.php?amount=50&category=18").json()['results']
    # geopraphy
    c = requests.get("https://opentdb.com/api.php?amount=50&category=22").json()['results']
    # history
    d = requests.get("https://opentdb.com/api.php?amount=50&category=23").json()['results']
    # animals
    e = requests.get("https://opentdb.com/api.php?amount=50&category=27").json()['results']

    # creating pseudo-random question order
    packages = []
    for i in range(50):
        b[i]['category'] = 'Computer Science'
        package = []
        package.append(a[i])
        package.append(b[i])
        package.append(c[i])
        package.append(d[i])
        package.append(e[i])
        random.shuffle(package)
        packages.append(package)
    random.shuffle(packages)

    questions = []
    for package in packages:
        for question in package:
            questions.append(question)

    questions_js = []
    correct_answers = []
    for question in questions:

        # combine correct and incorrect answers
        if len(question['incorrect_answers']) == 3:
            answers = question['incorrect_answers']
            answers.append(question['correct_answer'])
            random.shuffle(answers)
        else:
            answers = ['True', 'False']

        # prepare array to send to javascript
        questions_js.append({
            'answers' : answers,
            'question' : question['question'],
            'difficulty' : question['difficulty'],
            'category' : question['category'],
            'type' : question['type']
        })

        # keep track of all correct answers
        correct_answers.append(question['correct_answer'])

    # save correct answers to session
    session['correct_answers'] = correct_answers

    # return questions to frontend
    return jsonify(questions_js)



@app.route("/check_answer")
def check_answer():
    """Checks every answer of correctness"""

    # get answer from frontend
    answer = request.args.get('answer')
    question_data = json.loads(request.args.get('question_data'))
    correct_answer = session['correct_answers'][0]

    question_data['user_answer'] = answer
    question_data['correct_answer'] = correct_answer
    session['question_results'].append(question_data)

    # get correct answer
    correct_answer = session['correct_answers'][0]
    session['correct_answers'].remove(session['correct_answers'][0])

    # check if answer is correct and keep track of indiviual scores and return true
    if answer == correct_answer:
        session["category_scores"][question_data['category']]+= 1
        session["difficulty_scores"][question_data['difficulty']]+= 1
        session["type_scores"][question_data['type']]+= 1
        return jsonify(True)
    # if answer is not correct return False
    else:
        return jsonify(False)



@app.route("/chart_values")
def chart_values():
    """returns chart data after user finishes quiz"""
    return jsonify(session['chart_data'])



@app.route("/deletebutton_display")
def deletebutton_display():
    """hides or shows delete username button"""

    # check if user has user id in current session
    try:
        session['user_id']
    # if not, return False (button will not show)
    except:
        return jsonify(False)

    # if session is found True returns (button will show)
    return jsonify(True)


@app.route("/questions")
def questions():
    return render_template('question_results.html', data=session['question_results'])