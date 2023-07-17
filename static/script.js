var map = L.map('map').setView([0, 0], 20);  // Establecer el zoom en 20

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var customIcon = L.icon({
    iconUrl: 'https://i.ibb.co/RcyK0M0/1.png',
    iconSize: [80, 80],
    iconAnchor: [12, 41]
});

var marker = L.marker([0, 0], { icon: customIcon });

var interval;

function startPinChange() {
    if (interval) {
        return;
    }
    var i = 1;
    interval = setInterval(function () {
        if (i < coordenadas.length) {
            marker.setLatLng(coordenadas[i]);
            map.setView(coordenadas[i], 17);  // Centrar el mapa en la coordenada actual

            var coordInicial = coordenadas[0];
            var coordFinal = coordenadas[coordenadas.length - 1];
            var coordActual = coordenadas[i];

            document.getElementById('initialCoordinate').innerHTML = "<strong>Coordenada inicial:</strong> " + coordInicial;
            document.getElementById('finalCoordinate').innerHTML = "<strong>Coordenada final:</strong> " + coordFinal;
            document.getElementById('currentCoordinate').innerHTML = "<strong>Coordenada actual:</strong> " + coordActual;

            i++;
        } else {
            clearInterval(interval);
            interval = null;
            document.getElementById('startButton').disabled = false;
            document.getElementById('stopButton').disabled = true;
        }
    }, 2000);
    document.getElementById('startButton').disabled = true;
    document.getElementById('stopButton').disabled = false;
}

function stopPinChange() {
    if (interval) {
        clearInterval(interval);
        interval = null;
        document.getElementById('startButton').disabled = false;
        document.getElementById('stopButton').disabled = true;
    }
}

document.getElementById('startButton').addEventListener('click', startPinChange);
document.getElementById('stopButton').addEventListener('click', stopPinChange);

marker.addTo(map);
