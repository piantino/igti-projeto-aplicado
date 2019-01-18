import flask
import json
import os

import crawler
import classificador

rotulos = ['EXP', 'BAN', 'OIG', 'DAN', 'SEG', 'CON']

classificador = classificador.Classificador(rotulos)
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

    return flask.render_template('index.html', lista=lista, processo=processo, rotulos=rotulos)

def validar_processo(processo):
    raise ValueError('Implementar')

if __name__ == "__main__":
    app.run(port=os.environ.get('PORT', 5000))