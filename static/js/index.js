document.getElementById("quiz_header").style.display = "none";

function toggle_guide(){
    guide = document.getElementById("quiz_guide");
    if(guide.style.display === "none"){
        guide.style.display = "block";
    }
    else{
        guide.style.display = "none";
    }
}