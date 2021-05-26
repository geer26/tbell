
socket = io();

switch_pane('users', $('#users_icon'));


function switch_pane(pane, e=null){

    $("div.pane").hide();

    $("i.fas").removeClass('menuicon-active-pane');

    if (e){
        console.log("HELLO!");
    }

}