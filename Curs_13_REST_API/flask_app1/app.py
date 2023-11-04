from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


# GET
@app.route("/")
def index():
    return "ok"


@app.route('/date')
def get_date():
    date = datetime.now().date().isoformat()
    return date


@app.route('/time')
def get_time():
    time = datetime.now().time().isoformat()
    return f'Este ora: {time}'


@app.route('/hello/<name>')
def hello(name):
    return f"Hello {name}"


# POST
@app.route('/login', methods=["POST"])
def login():
    print(request.method)
    print(request.json)  # se afiseaza datele trimise ca payload in request
    # variabila request este o variabila globala din pachetul Flask care retine date despre requestul curent
    return "Ok"


# PUT
@app.route('/login', methods=["PUT"])
def login_put():
    data = request.json
    return jsonify(data) #utila pentru a returna resurse sub forma de json


# cand rulam codul dintr-un fisier, valoarea fisierului se modifica din numele fisierului in main
if __name__ == '__main__':
    app.run(debug=True)  # debug = restart aplicatie la fiecare modificare
    # codul din acest if va fi rulat doar cand aplicatia porneste din fisierul curent.
    # atributul __name__ ia valoarea __main__ doar cand aplicatia este rulata din fisierul curent
