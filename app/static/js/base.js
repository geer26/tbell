function toggle_visibility(elem) {
    var x = document.getElementById(elem);
    if (x.style.display === "none") {
        x.style.display = "inline-block";
    } else {
        x.style.display = "none";
    }
}

function fetch_hello(){
    fetch('/api')
    .then(response => response.json())
    .then(data => {
        console.log(data);
    });
}