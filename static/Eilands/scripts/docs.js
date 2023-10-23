var socket = io();

socket.on('new_eiland', function() {
  get_count();
});


function get_count(){
  $.getJSON(("/eilands/count"), function(response){
         document.getElementById("eiland_count").innerHTML = "<span class='eiland_count'>"+response+"</span>";
              }
          )}

function buildindex(){
  $('#docscontent').find('h1').each(function(){
    var innerDivId = $(this).attr('id');
    var name =  document.getElementById(innerDivId).innerHTML;
    document.getElementById("docsindex").innerHTML += "<h2 style='cursor: pointer' onclick='scrollto("+innerDivId+")'>"+name+"</h2>";
});
}


function scrollto(divid){
  document.getElementById(divid).scrollIntoView();
}
