let lng;
let lat;

mapboxgl.accessToken =
    'pk.eyJ1Ijoiam95am95am95eSIsImEiOiJja2w4YzZyM3kxcTdmMnZwZXdiNG5yczRjIn0.CDJtfCb3X8TKcTBRMPBJFA';
var coordinates = document.getElementById('coordinates');

var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-1.527581244588987 , 43.130288226235024], //[lng, lat] format
    zoom: 2,
    minZoom: 1.39
});

//make popup variable with button embedded
let popup = new mapboxgl.Popup({ offset: 25 }) // add popups
    .setHTML('<button class="btn">Current location</button>')

//create blue marker and add to the map
var marker = new mapboxgl.Marker({
        draggable: true
    })
    .setLngLat([8.301137874032406 , 47.35344426456044]) //[lng, lat] format
    .setPopup(popup)
    .addTo(map);

//displays coords when marker is finishes moving
marker.on('dragend', onDragEnd);

//display coordinates depending on marker location on canvas
function onDragEnd() { 
    var lngLat = marker.getLngLat();
    lng = lngLat.lng
    lng = adjustLng(lng)
    lat = lngLat.lat

    // display coordinates on form side
    $('#lat').text(`Latitude: ${lat}`)
    $('#lng').text(`Longitude: ${lng}`)

    // //store data into session
    sessionStorage.setItem("coord_lat", JSON.stringify({ "lat": lat }))
    sessionStorage.setItem("coord_lng", JSON.stringify({"lng": lng }))
}

//wait for map to load, before buttons can be clicked
//not implemented in current view yet
map.on('load', function () {
    //click event inside 
    $('#map').on('click', '.btn', function() {
        alert('test');
    });
})



// adjust 0-360 coords to 180 to -180
function adjustLng(long) {
    if (long > 180) {
        long = long - 360
        return long
    }
    else if (long < -180) {
        long = long + 360
    }
    return(long)
}