console.log("Hello World!");

socket = io();


switch_pane('users');


function switch_pane(pane){

    $(".pane").each(function() {
        $(this).hide();
    });

    $('#'+pane).show();

}