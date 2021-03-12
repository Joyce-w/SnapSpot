//get sessionStorage info
const session_lat = sessionStorage.getItem('coord_lat')
const session_lng = sessionStorage.getItem('coord_lng')


const json_lat = JSON.parse(session_lat)
const json_lng = JSON.parse(session_lng)

let lng = (json_lng.lng)
lng = adjustLng(lng)

$('#coord_lat').val(json_lat.lat)
$('#coord_lng').val(lng)


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