// Fetch outcome of backend check for session
fetch("/button_display")
  .then((response) => {
    return response.json();
  })

  // Display results and delete button when appropriate
  .then((session) => {
  if (session == "deleted") {
    document.getElementById("results").style.display = "block";
  }
  else if (session == true){
    document.getElementById("delete_score").style.display = "block";
    document.getElementById("results").style.display = "block";
  }
});

