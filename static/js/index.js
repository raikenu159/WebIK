document.getElementById("quizHeader").style.display = "none";

function toggle_guide(){
    guide = document.getElementById("quizGuide");
    if(guide.style.display === "none"){
        guide.style.display = "block";
    }
    else{
        guide.style.display = "none";
    }
}