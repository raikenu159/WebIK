// Fetch outcome of backend check for session
fetch("/button_display")
  .then((response) => {
    return response.json();
  })

  // Display delete score button if session exists
  .then((session) => {
  if (session == true){
    document.getElementById("delete_score").style.display = "block";
    document.getElementById("results").style.display = "block";
  }
});

