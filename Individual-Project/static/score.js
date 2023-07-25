let arr = ["washington", "uuu",
    "Geeks", "Computer Science Portal"];
 
function random_country() {
    console.log(arr[(Math.floor(Math.random() * arr.length))]);
}

random_country()
