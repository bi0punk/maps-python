var map = L.map('map').setView([-28.579, -70.742], 16);
        var circle = L.circle([-28.581151132402457, -70.74742180606718], {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5,
            radius: 50
        }).addTo(map);
        var polygon = L.polygon([
            [-28.577697780133278, -70.73972919381356],
            [-28.578597551844357, -70.7399115840282],
            [-28.57821597420524, -70.73888161575726]
        ]).addTo(map);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
            maxZoom: 18,
        }).addTo(map);

        $.get('/api/coordinates', function(response) {
            var coordenadas = response.coordenadas;

            var myIcon = L.icon({
                iconUrl: 'https://i.ibb.co/RcyK0M0/1.png',
                iconSize: [50, 50],
                iconAnchor: [16, 32],
            });

            var index = 0;
            var marker;
            var timeoutId;

            function displayNextCoordinate() {
                var coordinates = coordenadas[index];
                var lat = coordinates[0];
                var lon = coordinates[1];

                if (marker) {
                    marker.setLatLng([lat, lon]);
                } else {
                    marker = L.marker([lat, lon], { icon: myIcon }).addTo(map);
                }

                index++;
                if (index < coordenadas.length) {
                    timeoutId = setTimeout(displayNextCoordinate, 3000);  // Retraso de 3 segundos entre cada coordenada
                }
            }

            function startSequence() {
                if (!timeoutId && index < coordenadas.length) {
                    displayNextCoordinate();
                }
            }

            function stopSequence() {
                clearTimeout(timeoutId);
                timeoutId = null;
            }

            function resetSequence() {
                clearTimeout(timeoutId);
                timeoutId = null;
                index = 0;
                if (marker) {
                    marker.setLatLng(coordenadas[index]);
                }
            }

            $('#startButton').click(startSequence);
            $('#stopButton').click(stopSequence);
            $('#resetButton').click(resetSequence);
        });