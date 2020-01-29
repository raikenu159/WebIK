import os
import requests
import random
import json
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp


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

    # Forget any session
    session.clear()

    # Create table scores in database
    db.execute("CREATE TABLE if not exists 'scores' ('id' integer NOT NULL PRIMARY KEY, 'username' varchar(16), 'score' integer, 'date' DATE DEFAULT CURRENT_DATE)")

    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    """Take quiz"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Get the username from the frontend
        session["username"] = request.form.get("username")

        return redirect("/leaderboard")

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # Forget any session
        session.clear()

        # Set the category, difficulty and type sessions equal to 0
        session["category_scores"] = {
        "General Knowledge" : 0,
        "Computer Science" : 0,
        "Geography" : 0,
        "History" : 0,
        "Animals" : 0
        }
        session["difficulty_scores"] = {
        "easy" : 0,
        "medium" : 0,
        "hard" : 0
        }
        session["type_scores"] = {
        "boolean" : 0,
        "multiple" : 0
        }
        session["question_results"] = []

        return render_template("quiz.html")


@app.route("/check", methods=["GET"])
def check():
    """Return true if achieved score is in top 10"""

    # Get user score from frontend and update into DB
    session["score"] = int(request.args.get("score"))
    session["inserted"] = False

    leaderboard = db.execute("SELECT score FROM scores")

    # Check position in current leaderboard and give the output for the position of the user
    ranking = 1
    for score in leaderboard:
        if session["score"] <= score["score"]:
            ranking+= 1

    if ranking <= 10:
        return jsonify(["Congratulations! you are number " + str(ranking) + " on the leaderboard.", True])
    else:
        percentile = ((1-(ranking / len(leaderboard))) * 100)

        if percentile > 50:
            return jsonify("Well done you scored better than {0:.2f}% of previous users!".format(percentile))
        elif percentile >= 25:
            return jsonify("You scored better than {0:.2f}% of previous users.".format(percentile))
        elif percentile < 25:
            return jsonify("Better luck next time, you scored in the bottom quartile.")


@app.route("/leaderboard")
def leaderboard():
    """Display the current leaderboard and some statistics about the users performance"""

    # Select the top 10 scores from the scores database
    topscores = db.execute("SELECT * FROM scores ORDER BY score DESC, id ASC LIMIT 10")

    # Check if the user has already played the quiz: if not display button 'play now'
    try:
        session["score"]
    except:
        return render_template("leaderboard.html", scores=topscores, played="Play now!")

    # Display button 'try again' if the user didn't reach the top 10 leaderboard
    if session["inserted"] == True:
        return render_template("leaderboard.html", scores=topscores, played="Try again!")

    # Check if the user has filled in a username: if not add the score to the database
    try:
        session["username"]
    except:
        row = db.execute("INSERT INTO scores (score) VALUES (:score)", score=session["score"])
        session["inserted"] = True
        session["user_id"] = row
        topscores = db.execute("SELECT * FROM scores ORDER BY score DESC, id ASC LIMIT 10")
        return render_template("leaderboard.html", scores=topscores, played="Try again!")

    # If the user has played the quiz but did not make the topscores display "try again"
    row = db.execute("INSERT INTO scores (score, username) VALUES (:score, :username)", score=session["score"], username=session["username"])
    session["inserted"] = True
    session["user_id"] = row
    topscores = db.execute("SELECT * FROM scores ORDER BY score DESC, id ASC LIMIT 10")
    return render_template("leaderboard.html", scores=topscores, played="Try again!")


@app.route("/delete_username")
def delete_username():
    """Delete the username of the user from the leaderboards"""

    # Delete the score from the database
    db.execute("DELETE FROM scores WHERE id=:id", id=session["user_id"])

    return redirect("/leaderboard")


@app.route("/barchart")
def barchart():
    """Display in a barchart the score per category"""

    # Add all scores per category from current user's session
    category = [[score for score in session["category_scores"].values()], [name for name in session["category_scores"].keys()], "Category scores"]
    difficulty = [[score for score in session["difficulty_scores"].values()], [name for name in session["difficulty_scores"].keys()], "Difficulty scores"]
    types = [[score for score in session["type_scores"].values()], [name for name in session["type_scores"].keys()], "Type scores"]

    session["chart_data"] = [category, difficulty, types]

    return render_template("barchart.html")


@app.route("/load_questions", methods=["GET"])
def load_questions():
    """Fetches questions"""

    # Request questions from API per category
    general = requests.get("https://opentdb.com/api.php?amount=50&category=9").json()["results"]
    computers = requests.get("https://opentdb.com/api.php?amount=50&category=18").json()["results"]
    geography = requests.get("https://opentdb.com/api.php?amount=50&category=22").json()["results"]
    history = requests.get("https://opentdb.com/api.php?amount=50&category=23").json()["results"]
    animals = requests.get("https://opentdb.com/api.php?amount=50&category=27").json()["results"]

    # Creating pseudo-random question order
    packages = []
    for i in range(50):
        computers[i]["category"] = "Computer Science"
        package = [general[i], computers[i], geography[i], history[i], animals[i]]
        random.shuffle(package)
        packages.append(package)

    random.shuffle(packages)

    questions = []
    for package in packages:
        for question in package:
            questions.append(question)

    questions_js = []
    session["correct_answers"] = []
    for question in questions:

        # Combine correct and incorrect answers
        if len(question["incorrect_answers"]) == 3:
            answers = question["incorrect_answers"]
            answers.append(question["correct_answer"])
            random.shuffle(answers)
        else:
            answers = ["True", "False"]

        # Prepare array to send to javascript
        questions_js.append({
            "answers" : answers,
            "question" : question["question"],
            "difficulty" : question["difficulty"],
            "category" : question["category"],
            "type" : question["type"]
        })

        # Keep track of all correct answers
        session["correct_answers"].append(question["correct_answer"])

    # Return questions to frontend
    return jsonify(questions_js)


@app.route("/check_answer")
def check_answer():
    """Checks every answer of correctness"""

    # Get answer from frontend
    index = int(request.args.get("index"))
    answer = request.args.get("answer")
    correct_answer = session["correct_answers"][index]

    question_data = json.loads(request.args.get("question_data"))
    question_data["user_answer"] = answer
    question_data["correct_answer"] = correct_answer

    session['question_results'].append(question_data)

    # Check if answer is correct and keep track of indiviual scores and return True
    if answer == correct_answer:
        session["category_scores"][question_data["category"]]+= 1
        session["difficulty_scores"][question_data["difficulty"]]+= 1
        session["type_scores"][question_data["type"]]+= 1
        return jsonify(True)

    # If answer is not correct return False
    else:
        return jsonify(False)


@app.route("/chart_values")
def chart_values():
    """Returns barchart data"""

    return jsonify(session["chart_data"])


@app.route("/button_display")
def button_display():
    """Hides or shows 'delete username' and 'detailed results' buttons"""

    # Check if user has a session with a score
    try:
        session["score"]

    # If not, return False (button will not show)
    except:
        return jsonify(False)

    # If session is found return True (button will show)
    return jsonify(True)


@app.route("/questions")
def questions():
    """Loads the question results page"""

    return render_template("question_results.html")


@app.route("/question_results")
def question_results():
    """Returns question information"""

    return jsonify(session["question_results"])

