//get sessionStorage info
const dataString = sessionStorage.getItem('coords')
console.log(dataString)

const data = JSON.parse(dataString)
console.log(data)


$('#coords').text(`[${data.lat}, ${data.lng}]`)

