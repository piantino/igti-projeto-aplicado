import string
import re
from unidecode import unidecode
from stop_words import get_stop_words

class Limpeza(object):  

    def __init__(self):
        self.remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
        self.stop_words = get_stop_words("pt")
            

    def tratar_texto(self, texto):
        texto = texto.lower()
        texto = texto.replace('<br>', '')
        return texto

    def remover_pontuacao(self, texto):
        return texto.translate(self.remove_punctuation_map)

    def remover_stop_words(self, texto):
        words = [word for word in texto.split() if len(word) > 1 and word not in self.stop_words]
        return ' '.join(words)

    def normalizar(self, texto):
        texto = self.tratar_texto(texto)
        texto = self.remover_pontuacao(texto)
            
        # quebra em palavras
        texto = self.remover_stop_words(texto)
        
        # remover acentuação
        texto = unidecode(texto)
        
        #removendo números
        texto = re.sub('[^a-zA-Z ]+', '', texto)

        return texto