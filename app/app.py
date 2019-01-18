import flask
import json

import crawler

import classificador

classificador = classificador.Classificador(['EXP', 'BAN', 'OIG', 'DAN', 'SEG', 'CON'])
juris = crawler.Crawler()

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    lista = []
    processo = '' 

    if flask.request.args.get('processo'):
        processo = flask.request.args.get('processo')
        acordaos = juris.get_acordaos(processo)

        for acordao in acordaos:
            classes = classificador.classificar(acordao['ementa'])
            lista.append({'acordao': acordao, 'classes': classes})

    return flask.render_template('index.html', lista=lista, processo=processo)

if __name__ == "__main__":
    app.run()