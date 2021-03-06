import flask
import json
import os
import re

import crawler
import classificador
import classificador_leis

rotulos = {
    'BAN': 'Bancário',
    'CON': 'Contratos',
    'DAN': 'Dano, Responsabilidade Civil',
    'EXP': 'Expurgos Cumprimento',
    'OIG': 'OI Conhecimento',
    'OIE': 'OI Execução de Sentença',
    'SEG': 'Seguros em geral'
}

clf = classificador.Classificador(list(rotulos.keys()))
clf_lei = classificador_leis.ClassificadorLeis()
juris = crawler.Crawler()

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    lista = []
    processo = '' 

    if flask.request.args.get('processo'):
        processo = formatar_num_processo(flask.request.args.get('processo'))
        acordaos = juris.get_acordaos(processo)

        for acordao in acordaos:
            
            lista.append(classificar(acordao))

    return flask.render_template('index.html', lista=lista, processo=processo, rotulos=rotulos)

def classificar(acordao):
    classes = clf.classificar(acordao['ementa'])
    classe_lei, leis = clf_lei.classificar(acordao['ementa'])

    if len(classes) == 0:
        classe = classe_lei
    else:
        classe = classes[0]
         
    if leis:
        leis = list(set(leis))

    return {'acordao': acordao, 'classe': classe, 'classes': classes, 'classe_lei': classe_lei, 'leis': leis}

def formatar_num_processo(processo):
    num = re.sub('[^\d]', '', processo)
    
    if len(num) != 20:
        raise ValueError('Número inválida de processo')
    m = re.search('(\d{7})(\d{2})(\d{4})(\d)(\d{2})(\d{4})', num)
    return '{0}-{1}.{2}.{3}.{4}.{5}'.format(m.group(1), m.group(2), m.group(3), m.group(4), m.group(5), m.group(6))

@app.errorhandler(ValueError)
def handle_invalid_usage(error):
    response = flask.jsonify(str(error))
    response.status_code = 400
    return response

if __name__ == "__main__":
    app.run(port=os.environ.get('PORT', 5000))