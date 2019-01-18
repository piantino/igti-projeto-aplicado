from limpeza import Limpeza
import load_models

class Classificador(object):
    def __init__(self, rotulos):
        self.pipelines = load_models.Loader().get_pipelines(rotulos)        
        self.nomalizador = Limpeza()
        
    def classificar(self, ementa):
        texto = self.nomalizador.normalizar(ementa)
    
        classes = []
        for p in self.pipelines:
            resultado = p.predict([texto])
            if resultado != 'NONE':
                classes.append(resultado[0])
        
        return classes

