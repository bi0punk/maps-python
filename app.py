from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Lista de coordenadas predefinidas
lista_coordenadas = [
    [-28.578254049177758, -70.73962682573982],
    [-28.578556224309416, -70.74044884000381],
    [-28.579034666492436, -70.74126129596239],
    [-28.57950471283357, -70.74249431735838],
    [-28.57975652250934, -70.74322074856843],
    [-28.580251746446315, -70.74393762147307],
    [-28.58037765046529, -70.74498903506654],
    [-28.580713393779057, -70.74600221543844],
    [-28.580688213067702, -70.74624117307332],
    [-28.580881265034005, -70.74681467139702],
    [-28.581139335273047, -70.7474228957248]
]

@app.route('/')
def coordenadas():
    return render_template('index.html')

@app.route('/api/coordinates')
def api_coordinates():
    return jsonify(coordenadas=lista_coordenadas)

if __name__ == '__main__':
    app.run(debug=True)
