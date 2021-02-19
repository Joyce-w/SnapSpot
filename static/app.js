


mapboxgl.accessToken =
    'pk.eyJ1Ijoiam95am95am95eSIsImEiOiJja2w4YzZyM3kxcTdmMnZwZXdiNG5yczRjIn0.CDJtfCb3X8TKcTBRMPBJFA';

var map = new mapboxgl.Map({
    container: 'map', // container ID
    style: 'mapbox://styles/mapbox/outdoors-v11', // style URL
    center: [-118.1661, 33.9446], // starting position [lng, lat]
    zoom: 8 // starting zoom
});

//Creates a geocoder
map.addControl(
    new MapboxGeocoder({
        accessToken: mapboxgl.accessToken,
        mapboxgl: mapboxgl
    })

);

var marker = new mapboxgl.Marker()
.setLngLat([-122.414, 37.776])
    .addTo(map);

new mapboxgl.Marker()
.setLngLat([-122.414, 37.776])
.setPopup(new mapboxgl.Popup({ offset: 25 }) // add popups
.setHTML('<p>popup box </p>'))
.addTo(map);