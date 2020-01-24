// initiate global variables
var score = 0;
var timer = 60;
var question_index = 0;
var questions;
var question_data;
var difficulty_score;
var difficulty;
var type;
var category;
var checked = false;

// hide top10 popup when starting quiz
document.getElementById("top10form").style.display = "none";
document.getElementById("quizScreen").style.display = "none";


// open popup if in top10
function openPopup() {
  document.getElementById("top10form").style.display = "block";
  // document.getElementById("question").style.display = "none";
  // document.getElementById("all_answers").style.display = "none";
  // document.getElementById("stop").style.display = "none";
  document.getElementById("quizScreen").style.display = "none";
  document.getElementById('score2').innerHTML = "Score:" + " " + score;
}


// display default values of the timer and score (60, 0)
document.getElementById('time').innerHTML = timer;
document.getElementById('score').innerHTML = "Score:" + " " + score;

// generate a question
load_questions();


// decrement time every second
setInterval(countdown, 1000);


// check the answer
function check(input) {
  console.log(question_data)
  fetch('/check_answer?answer='+input+'&question_data='+encodeURIComponent(JSON.stringify(question_data)))
  .then((response) => {
      return response.json();
  })

  .then((data) => {
  if (data == true) {
    // if answer correct increment score
    score++;

    // add the amount of time appropriate for the difficulty of the question
    timer = timer + difficulty_score;

    // display time added to timer
    document.getElementById('timer_change').innerHTML = "+" + difficulty_score;

    // turn the background of the time green to make the time increment visible
    document.getElementById("timer_color").style.backgroundColor = "LawnGreen";

    // display the incremented score
    document.getElementById('score').innerHTML = "Score:" + " " + score;
  }
  // else if answer not correct
  else {
    // subract the amount of time
    timer = timer + (difficulty_score - 4);

    //display time subtracted from timer
    document.getElementById('timer_change').innerHTML = (difficulty_score - 4);

    // display time is subtraction from timer
    document.getElementById("timer_color").style.backgroundColor = "red";
  }
  question_index++;

  // generate a new question
  next(questions);

  // return timer to default color after a short time
  setTimeout(reset_color, 700);
  });
}



// reset timer backgroundcolor and remove displayed incremented/subtracted time
function reset_color() {
  document.getElementById("timer_color").style.backgroundColor = "white";
  document.getElementById("timer_change").innerHTML = " ";
}



// decrement timer if page loaded or end quiz if time is up
function countdown() {
  if (!document.getElementById('answer4').innerHTML) {
    return;
  }
  else if (timer >= 0) {
    document.getElementById("quizScreen").style.display = "block";
    document.getElementById('time').innerHTML = timer;
    timer--;
  }
  else if (timer <= 0) {
    if (!checked) {
      check_score();
    }
  }
  document.getElementById("loader").style.display = "none";
}



function check_score() {
  //stop timer at 0
  if (timer < 0) {
    document.getElementById('time').innerHTML = 0;
    // fetch response from backend for position in leaderboard
    fetch('/check?score=' + score)
    .then((response) => {
      return response.json();
    })

    .then((data) => {
      // var check_executed == True; | user is in top 10: display popup
      if (data.length == 2) {
        openPopup();
        checked = true;
      }
      // user not in top10: alert with information on position ("better than X% of players")
      else {
        alert(data);
        checked = true;
        location.replace("/leaderboard");
      }
    });
  }
}



// fetch questions from backend
function load_questions() {
  fetch('/load_questions')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    questions = data;
    next(questions);
  });
}



function next(data) {
    // define question variables
    Question = data[question_index];
    question_data = Question;
    category = Question.category;
    difficulty = Question.difficulty;
    type = Question.type;

    // add and subtract different amount of time per question difficulty
    if (Question.difficulty == "easy") {
      difficulty_score = 1;

      // also display icon showing difficulty per question
      document.getElementById("difficulty").innerHTML = "<img src='/static/difficulty_easy.png' alt='difficulty_easy icon'>";
    }
    else if (Question.difficulty == 'medium') {
      difficulty_score = 2;
      document.getElementById("difficulty").innerHTML = "<img src='/static/difficulty_medium.png' alt='difficulty_medium icon'>";
    }
    else {
      difficulty_score = 3;
      document.getElementById("difficulty").innerHTML = "<img src='/static/difficulty_hard.png' alt='difficulty_hard icon'>";
    }

    let answers = Question.answers;

    // remove the 3rd and 4th button if True/False question
    if (Question.answers.length == 2) {
      document.getElementById('answer3').style.display = "none";
      document.getElementById('answer4').style.display = "none";
    }
    else {
      document.getElementById('answer3').style.display = "block";
      document.getElementById('answer4').style.display = "block";
    }
    // displaying question and answers
    document.getElementById('question').innerHTML = Question.question;
    document.getElementById('answer1').innerHTML = answers[0];
    document.getElementById('answer2').innerHTML = answers[1];
    document.getElementById('answer3').innerHTML = answers[2];
    document.getElementById('answer4').innerHTML = answers[3];
    document.getElementById('category').innerHTML = 'Category: ' + Question.category;
}



// skip to next question
function skip_question() {
  question_index++;
  next(questions);
}


