


mapboxgl.accessToken =
    'pk.eyJ1Ijoiam95am95am95eSIsImEiOiJja2w4YzZyM3kxcTdmMnZwZXdiNG5yczRjIn0.CDJtfCb3X8TKcTBRMPBJFA';

var map = new mapboxgl.Map({
    container: 'map', // container ID
    style: 'mapbox://styles/mapbox/outdoors-v11', // style URL
    center: [-118.1661, 33.9446], // starting position [lng, lat]
    zoom: 8 // starting zoom
});

// testing py data
   function test_func(point) {
        console.log(point);
    }
    test_func({{ point|safe }})
    console.log(test_func({{ point|safe }}))


//Creates a search with geocoding
map.addControl(
    new MapboxGeocoder({
        accessToken: mapboxgl.accessToken,
        mapboxgl: mapboxgl
    })

);

// adds marker at set location
var marker = new mapboxgl.Marker()
    .setLngLat([-122.414, 37.776])
    .setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
    .setHTML('<p>popup box </p>'))
    .addTo(map);

