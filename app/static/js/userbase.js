preload_end();


function fetch_hello(){
    fetch('/api')
    .then(response => response.json())
    .then(data => {
        console.log(data);
     });
}