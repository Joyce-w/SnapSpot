
const button = document.getElementById('btn')
let lng;
let lat;

mapboxgl.accessToken =
    'pk.eyJ1Ijoiam95am95am95eSIsImEiOiJja2w4YzZyM3kxcTdmMnZwZXdiNG5yczRjIn0.CDJtfCb3X8TKcTBRMPBJFA';
var coordinates = document.getElementById('coordinates');
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [0, 0],
    zoom: 2
});

var marker = new mapboxgl.Marker({
        draggable: true
    })
    .setLngLat([0, 0])
    .setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
    .setHTML('<button id="btn"><a href="/new-post">Share location</a></button'))
    .addTo(map);

marker.on('dragend', onDragEnd);


function onDragEnd() { 
    var lngLat = marker.getLngLat();
    coordinates.style.display = 'block';
    coordinates.innerHTML =
    'Longitude: ' + lngLat.lng + '<br />Latitude: ' + lngLat.lat;
    lng = lngLat.lng
    lat = lngLat.lat
    console.log(lng, lat)

}


    // even listener for click button in marker
button.on('click', function (lat,lng) {
    //send axios data to python
    
    
    
})
