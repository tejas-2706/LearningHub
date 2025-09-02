// frontend
const socket = io();

if (navigator.geolocation) {
    navigator.geolocation.watchPosition(
    (position) => {
        const {latitude, longitude} = position.coords;
        socket.emit("send-location", {latitude,longitude});
    }, 
    (error) => {
        console.error(error);
    }, 
    {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0
    });
}

const map = L.map("map").setView([0,0],10);
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: 'tejasMap'
}).addTo(map);

const markers = {};

socket.on("receive-location", (data) => {
    const {id, latitude, longitude} = data;
    console.log("Received data from ID:", id); // Verify ID is unique

    map.setView([latitude,longitude],16);
    if(markers[id]){
        markers[id].setLatLng([latitude,longitude]);
    }else {
        markers[id] = L.marker([latitude,longitude]).addTo(map);
        if (id === socket.id){
            markers[id].bindTooltip("You", {permanent: true, direction: "bottom"}).openTooltip();
        }
    }
});

socket.on("user-disconnect", (id) => {
    if (markers[id]){
        map.removeLayer(markers[id]);
        delete markers[id];
    }
});

console.log(markers);
