preload_end();


function fetch_hello(){
    preload_start();
    fetch('/api')
    .then(response => response.json())
    .then(data => {
        preload_end();
        console.log(data);
     });
}


function hide_sidebar(){
    $('.user-sidebar').css('left', '-30vw');
    setTimeout(() => { $('.user-sidebar').css('left',''); }, 400);
    return;
}