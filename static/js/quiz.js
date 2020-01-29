// Initiate global variables
var score = 0;
var timer = 60;
var question_index = 0;
var questions;
var question_data;
var difficulty_score;
var checked = false;


// Open popup if in top10
function openPopup() {
  document.getElementById("top10form").style.display = "block";
  document.getElementById("quizScreen").style.display = "none";
  document.getElementById('final_score').innerHTML = "Score:" + " " + score;
}


// Display default values of the timer and score (60, 0)
document.getElementById('time').innerHTML = timer;
document.getElementById('score').innerHTML = "Score:" + " " + score;


// Generate a question
load_questions();


// Decrement time every second
setInterval(countdown, 1000);


// Check the users' given answer
function check(input) {
  fetch('/check_answer?answer='+input+'&question_data='+encodeURIComponent(JSON.stringify(question_data))+'&index='+question_index.toString())
  .then((response) => {
      return response.json();
  })

  .then((data) => {
  if (data == true) {
    // If answer correct increment score
    score++;

    // Add the amount of time appropriate for the difficulty of the question
    timer = timer + difficulty_score;

    // Display time added to timer
    document.getElementById('timer_change').innerHTML = "+" + difficulty_score;

    // Turn the background of the time green to make the time increment visible
    document.getElementById("timer_change").style.backgroundColor = "LawnGreen";

    // Display the incremented score
    document.getElementById('score').innerHTML = "Score:" + " " + score;
  }
  else {
    // Subtract time if answer is incorrect
    timer = timer + (difficulty_score - 4);

    //Display time subtracted from timer
    document.getElementById('timer_change').innerHTML = (difficulty_score - 4);

    // Display time is subtraction from timer
    document.getElementById("timer_change").style.backgroundColor = "red";
  }
  question_index++;

  // Generate a new question
  next(questions);

  // Return timer to default color after a short time
  setTimeout(reset_color, 700);
  });
}



// Reset timer backgroundcolor and remove displayed incremented/subtracted time
function reset_color() {
  document.getElementById("timer_change").style.backgroundColor = "white";
  document.getElementById("timer_change").innerHTML = " ";
}



// Decrement timer if page loaded or end quiz if time is up
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
  // Stop timer at 0
  if (timer < 0) {
    document.getElementById('time').innerHTML = 0;
    // Fetch response from backend for position in leaderboard
    fetch('/check?score=' + score)
    .then((response) => {
      return response.json();
    })

    .then((data) => {
      // Display popup if user is in top 10
      if (data.length == 2) {
        openPopup();
        checked = true;
      }
      // User not in top10: alert with information on position ("better than X% of players")
      else {
        alert(data);
        checked = true;
        location.replace("/leaderboard");
      }
    });
  }
}



// Fetch questions from backend
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
    // Define question variables
    Question = data[question_index];
    question_data = Question;
    category = Question.category;
    difficulty = Question.difficulty;
    type = Question.type;

    // Add and subtract different amount of time per question difficulty
    if (Question.difficulty == "easy") {
      difficulty_score = 1;

      // Display icon showing difficulty per question
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

    // Remove the 3rd and 4th button if True/False question
    if (Question.answers.length == 2) {
      document.getElementById('answer3').style.display = "none";
      document.getElementById('answer4').style.display = "none";
    }
    else {
      document.getElementById('answer3').style.display = "block";
      document.getElementById('answer4').style.display = "block";
    }
    // Display question and answers
    document.getElementById('question').innerHTML = Question.question;
    document.getElementById('answer1').innerHTML = answers[0];
    document.getElementById('answer2').innerHTML = answers[1];
    document.getElementById('answer3').innerHTML = answers[2];
    document.getElementById('answer4').innerHTML = answers[3];
    document.getElementById('category').innerHTML = 'Category: ' + Question.category;
}



// Skip to next question
function skip_question() {
  question_index++;
  next(questions);
}


