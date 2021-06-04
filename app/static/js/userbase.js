preload_end();
switch_pane('workouts_pane');
hide_modalbar();


function fetch_hello(){
    hide_sidebar();
    preload_start();
    fetch('/api')
    .then(response => response.json())
    .then(data => {
        preload_end();
        console.log(data);
     });
}


function hide_sidebar(){
    var x = window.matchMedia("(max-width: 600px)").matches;
    if (x){
        $('.user-sidebar').css('left', '-80vw');
        setTimeout(() => { $('.user-sidebar').css('left',''); }, 600);
    } else{
        $('.user-sidebar').css('left', '-30vw');
        setTimeout(() => { $('.user-sidebar').css('left',''); }, 400);
    }
    return;
}


//right side of the screen
function hide_modalbar(activeform){
    var x = window.matchMedia("(max-width: 600px)").matches;
    $('#'+activeform).show();
    if (x){
        $('.f-modalback').css('right', '-100%');
        setTimeout(() => {
            $('.user-sidebar').css('right','');
            $('#back').hide();
        }, 600);
    } else{
        $('.f-modalback').css('right', '-100%');
        setTimeout(() => {
            $('.user-sidebar').css('right','');
            $('#back').hide();
        }, 400);
    }
    return;
}


function show_modalbar(){
    $('.f-modalback').css('right', '0');
    $('#back').show();
}


function switch_pane(pane){
    $("div.cont").hide();
    $('#'+pane).show();
    activepane = pane;
    hide_sidebar();
}

