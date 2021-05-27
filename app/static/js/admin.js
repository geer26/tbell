
socket = io();

switch_pane('users');


function switch_pane(pane){

    $("div.pane").hide();

    $("i.fas").removeClass('menuicon-active-pane');

    console.log(pane);
    $('#'+pane).show();
    $('#'+pane+'_icon').addClass('menuicon-active-pane');

}