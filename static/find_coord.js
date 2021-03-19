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


//create blue marker and add to the map
var marker = new mapboxgl.Marker({
    draggable: true,
    color: "#1338BE"
    })
    .setLngLat([8.301137874032406 , 47.35344426456044]) //[lng, lat] format
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