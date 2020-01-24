  // hide 'delete username' button when loading page
  document.getElementById('delete-score').style.display = "none";
  document.getElementById('results').style.display = "none";

  // Fetch outcome of backend check for session
  fetch('/deletebutton_display')
    .then((response) => {
      return response.json();
    })

    // if outcome is True (session exists) display button
    .then((truefalse) => {
    console.log(truefalse)
    if (truefalse == true){
      document.getElementById('delete-score').style.display = "block";
      document.getElementById('results').style.display = "block";
    }
    })

