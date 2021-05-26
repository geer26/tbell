console.log("Hello World!");

socket = io();


switch_pane('users');


function switch_pane(pane){

    $(".pane").each(function(item) {
        $(item).hide();
        console.log(item);
    });

    $('#'+pane).show();

    console.log('#'+pane);

}