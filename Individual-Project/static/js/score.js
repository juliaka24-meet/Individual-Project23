var chosen_state = ""
let arr = ["washington", "uuu",
    "Geeks", "Computer Science Portal"];

function start_game(){
    var today = new Date();
    var start_time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
}
function random_state() {
    document.getElementById("state").innerHTML=(arr[(Math.floor(Math.random() * arr.length))]);
}

function check_state(chosen_state){
  if (document.getElementById("state").innerHTML== chosen_state){
    score ++;
    game_over()
  }
}

function game_over(){
  if (score==1){
    document.getElementById("result").innerHTML = "Good job!"
    var today = new Date();
    var end_time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    alert(end_time)
  }
}

