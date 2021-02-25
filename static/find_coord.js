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

//make popup variable with button embedded
let popup = new mapboxgl.Popup({ offset: 25 }) // add popups
    .setHTML('<button class="btn">Current location</button>')

//create blue marker and add to the map
var marker = new mapboxgl.Marker({
        draggable: true
    })
    .setLngLat([0, 0])
    .setPopup(popup)
    .addTo(map);

//displays coords when marker is finishes moving
marker.on('dragend', onDragEnd);

//display coordinates depending on marker location on canvas
function onDragEnd() { 
    var lngLat = marker.getLngLat();
    coordinates.style.display = 'block';
    coordinates.innerHTML =
    'Longitude: ' + lngLat.lng + '<br />Latitude: ' + lngLat.lat;
    lng = lngLat.lng
    lat = lngLat.lat

    // display coordinates on form side
    $('#lat').text(`Latitude: ${lat}`)
    $('#lng').text(`Longitude: ${lng}`)

    // //store data into session
    let data = { "lat": lat, "lng": lng }
    sessionStorage.setItem("coords", JSON.stringify(data))
}

//wait for map to load, before buttons can be clicked
//not implemented in current view yet
map.on('load', function () {
    //click event inside 
    $('#map').on('click', '.btn', function() {
        alert('test');
    });
})

