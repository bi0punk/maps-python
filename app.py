import json
import time
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def coordenadas():
    # Lista de coordenadas (ejemplo)
    lista_coordenadas = [
    [-28.575391, -70.740664],  # Coordenada inicial
    [-28.575811, -70.740781],
    [-28.576231, -70.740898],
    [-28.576651, -70.741015],
    [-28.577071, -70.741132],
    [-28.577491, -70.741249],
    [-28.577911, -70.741366],
    [-28.578331, -70.741483],  # Coordenada media
    [-28.578381, -70.744578],  # Coordenada adicional
    [-28.578441, -70.741563],
    [-28.578551, -70.741643],
    [-28.578661, -70.741723],
    [-28.578771, -70.741803],
    [-28.578881, -70.741883],
    [-28.578991, -70.741963],
    [-28.579101, -70.742043],
    [-28.579211, -70.742123],
    [-28.579321, -70.742203],
    [-28.579431, -70.742283],
    [-28.579541, -70.742363],
    [-28.579651, -70.742443],
    [-28.579761, -70.742523],
    [-28.579871, -70.742603],
    [-28.579981, -70.742683],
    [-28.580091, -70.742763],
    [-28.580311, -70.742891],
    [-28.581091, -70.747400]  # Coordenada final
]


    coordenadas_json = json.dumps(lista_coordenadas)
    return render_template('coordenadas.html', coordenadas=coordenadas_json)

if __name__ == '__main__':
    app.run(debug=True)



