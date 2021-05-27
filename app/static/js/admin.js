
socket = io();

switch_pane('users');

var activepane;


function switch_pane(pane){
    $("div.pane").hide();
    $("i.fas").removeClass('menuicon-active-pane');
    $('#'+pane).show();
    $('#'+pane+'_icon').addClass('menuicon-active-pane');
    activepane = pane;

}