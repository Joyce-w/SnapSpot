//get sessionStorage info
const dataString = sessionStorage.getItem('coords')
console.log(dataString)

const data = JSON.parse(dataString)
console.log(data)

let lng = (data.lng)
lng = adjustLng(lng)

$('#coords').val(`[${data.lat}, ${lng}]`)


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