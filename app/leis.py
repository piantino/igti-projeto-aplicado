import re

import load_models

class Leis(object):
    def get_leis(self, texto):
        texto = texto.lower()

        leis = []
        for lei in self.extrair_leis(texto):
            norm = self.normalizar_lei(lei)
            leis.append(norm)

        for art in self.extrair_artigos(texto):
            numero = art.replace('.', '')
            leis.append(numero)

        return leis

    def lei_valida(self, lei):
        return not re.match("^[\d\.]+/\d{3}$", lei)

    def extrair_leis(self, texto):
        terms = re.findall('\s(\d*\.?\d+\/\d{2,4})[^\d\/]', texto)
        return filter(self.lei_valida, list(set(terms)))

    def extrair_artigos(self, texto):
        texto = texto.replace('art.', 'artigo')
        terms = re.findall('\s(artigo \d*\.?\d+)', texto)
        return terms

    def normalizar_lei(self, lei):
        (numero, ano) = lei.split('/')
        return '{}/{}'.format(self.normalizar_numero(numero), self.normalizar_ano(ano))

    def normalizar_numero(self, numero):
        return int(numero.replace('.', ''))

    def normalizar_ano(self, numero):
        ano = int(numero)
        if (ano < 20):
            return '20' + numero
        if (ano < 100):
            return '19' + numero
        return numero