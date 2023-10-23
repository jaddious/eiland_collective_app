
var socket = io();

socket.on('new_eiland', function() {
  get_count();
});

var zoom;

var grayscale = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {});

var osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {});

var popp = L.tileLayer.wms("https://geoservices.informatievlaanderen.be/raadpleegdiensten/histcart/wms", {
  layers:'popp',
	format: 'image/png',
  version: '1.3.0',
	transparent: true,
	attribution: "Popp, Atlas cadastrale parcellaire de la Belgique, 1842 - 1879, Agentschap Informatie Vlaanderen",
  crs: L.CRS.EPSG3857
});

var ferraris = L.tileLayer.wms("https://geoservices.informatievlaanderen.be/raadpleegdiensten/histcart/wms", {
  layers:'ferraris',
	format: 'image/png',
  version: '1.3.0',
	transparent: true,
	attribution: "Ferrariskaart (1777), Vlaanderen",
  crs: L.CRS.EPSG3857
});

var ngi = new L.tileLayer("https://www.ngi.be/tiles/arcgis/rest/services/seamless_carto__default__3857__800/MapServer/tile/{z}/{y}/{x}", {
      minZoom: 7,
      maxZoom: 17
});

var map = L.map('map', {
zoomControl:false,
layers: [ngi]
});


function makemap(){
      var boundingpoints = [[50.7, 3.25],[50.9, 3.3]];
      var mapBounds = new L.LatLngBounds(boundingpoints);
      map.fitBounds(mapBounds);
};


function loadlayers(){

$.getJSON(("/eilands/all"), function(eilands) {
jQuery.each(eilands, function(i, eiland){

eiland.id = L.marker([eiland.y,eiland.x],
{title:eiland.Name,id:eiland.id,alt:eiland.Name,draggable:false,long:eiland.x,lat:eiland.y}).addTo(map).on('click',
  function(data){
      stopadding();
      map.flyTo(new L.LatLng(data.target.options.lat-0.001, data.target.options.long), 17);
      open_gallery(1);
      eiland_meta(data.target.options.id);
});

if (eiland.confirmation=='unconfirmed') {
  eiland.id.setIcon(unconfirmed_eiland)
} else {
  eiland.id.setIcon(confirmed_eiland)
}

})
})


}




function button1(){
  if($('#gallery1').css('display') === 'block')
{
  close_gallery(1);
}
else{
  open_gallery(1);
}}


function open_gallery(id){
  close_gallery(2);
  document.getElementById("gallery"+id).style.display = "block";
}

function close_gallery(id){
  document.getElementById("gallery"+id).style.display = "none";
}

function eiland_meta(id,x,y){
    $.ajax({
           type: "GET",
           url: "/eilands/"+id,
           contentType: "html",
           dataType: "text",
           success: function(response){
           document.getElementById("eiland_gallery").innerHTML = response;
                }
            });
  }

function get_count(){
  $.getJSON(("/eilands/count"), function(response){
         document.getElementById("eiland_count").innerHTML = "<span class='eiland_count'>"+response+"</span>";
              }
          )}

temp_eiland = L.marker([0,0])

function addeiland(){
  stopadding();
  $('.leaflet-container').css('cursor','crosshair');
  document.getElementById("eilandform").reset();
  map.on('click', function(e) {    map.off('click');
    document.getElementById("y").value = e.latlng.lat;
    document.getElementById("x").value = e.latlng.lng;
    $('.leaflet-container').css('cursor','pointer');
    temp_eiland = L.marker([e.latlng.lat,e.latlng.lng],{title:name,draggable:false,long:e.latlng.lng,lat:e.latlng.lat,icon:unconfirmed_eiland}).addTo(map)
})}

function stopadding(){
  map.off('click')
  $('.leaflet-container').css('cursor','pointer');
  map.removeLayer(temp_eiland)
  }




function resetform(){
  document.getElementById("eilandform").reset();
}


$(document).ready(function() {
    $('form').submit(function (e) {
        e.preventDefault();
    });
})


socket.on('new_eiland', function(response) {
  get_count();
  eiland = L.marker([response.y,response.x],
  {draggable:false,long:response.x,lat:response.y,icon:unconfirmed_eiland}).addTo(map).on('click',
    function(data){
        map.flyTo(new L.LatLng(data.target.options.lat-0.001, data.target.options.long), 17);
  });
});


function submiteiland(){
      var x=document.getElementById('x').value;
      var y=document.getElementById('y').value;
      var name=document.getElementById('name').value;
      var moat_situation=document.getElementById('moat_situation').value;


      $.ajax({
          type:"post",
          url:"/eilands/neweiland",
          data:
          {
             'name' :name,
             'moat_situation' :moat_situation,
             'x':x,
             'y':y
          },
          cache:false,
          success: function (html)
          {
          }
      });
      return false;
   }

globalThis.currentboard = 1;

function startonboarding(board){
  document.getElementById("onboarding").style.display = "block";
  document.getElementById(currentboard).style.display = "none";
  document.getElementById(board).style.display = "block";
  document.getElementById("circle"+currentboard).style.backgroundColor = "#DCDCDC";
  document.getElementById("circle"+board).style.backgroundColor = "black";
  globalThis.currentboard = board;
}

function nextboard(){
  if (parseInt(currentboard)+1==5) {
    stoponboarding();
    instruction1();
  }
  else {
  document.getElementById(currentboard).style.display = "none";
  startonboarding(parseInt(currentboard)+1);}
}

function stoponboarding(){
  document.getElementById(currentboard).style.display = "none";
  document.getElementById("onboarding").style.display = "none";
}

function getadress(x,y){
  console.log("/eilands/address/"+x+"/"+y)
  $.ajax({
         type: "GET",
         url: "/eilands/address/"+x+"/"+y,
         contentType: "html",
         dataType: "text",
         success: function(response){
          }
          });
}
