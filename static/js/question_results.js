// Get given questions and answers of user from application.py
fetch("/question_results")
        .then((response) => {
        return response.json();
        })
        .then((data) => {
        questions = data;
        questions.forEach(question => add_question(question))
        });


// Add one row to question results table
function add_question(question) {
  var table = document.getElementById("question_results_table");
  var row = table.insertRow(-1);
  var col1 = row.insertCell(0);
  var col2 = row.insertCell(1);
  var col3 = row.insertCell(2);
  col1.innerHTML = question.question;
  col2.innerHTML = question.user_answer;
  col3.innerHTML = question.correct_answer;

  // Color background of row green if question was correct. Otherwise color background red.
  if (question.correct_answer == question.user_answer){
      row.style.backgroundColor = "#ccffcc";
  }
  else{
      row.style.backgroundColor = "#ffcccc"
  }
}
