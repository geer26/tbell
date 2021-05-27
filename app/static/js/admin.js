
socket = io();


//standardized sender function
function send_message(message, namespace='admin'){
    socket.emit(namespace,message);
};


switch_pane('users');
refresh();

var activepane;


function switch_pane(pane){
    $("div.pane").hide();
    $("i.fas").removeClass('menuicon-active-pane');
    $('#'+pane).show();
    $('#'+pane+'_icon').addClass('menuicon-active-pane');
    activepane = pane;

}


function deluser(id){
    console.log(id);
    let message = {event: 1501, id: id};
    send_message(message);
}


function refresh(){

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {

    /*
    for (elem of document.querySelectorAll('.coll-content')){
        elem.style.display = "none";
    }
    */

    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}

}


//Websockets admin event dispatcher
socket.on('admin', function(data){

    switch (data['event']){

        //accept deluser status
        case 1502:{
            if (data['status'] != 1){
                console.log('ERROR MESSAGE');
                //DROP ERROR MESSAGE!
            } else {
                //console.log(data['content']);
                $('#users').remove();
                $('#maincontent').append(data['content']);
                refresh();
            }
            }
            break;

    }

});