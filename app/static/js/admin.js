
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


var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {

    for (elem of document.querySelectorAll('.coll-content')){
        elem.style.display = "none";
    }

    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}