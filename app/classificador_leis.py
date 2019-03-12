from leis import Leis
import load_models

class ClassificadorLeis(object):
    def __init__(self):
        self.pipeline = load_models.Loader().load_model('Modelo-Leis.pkl')
        self.features = load_models.Loader().load_model('Features-Leis.pkl')    
        self.nomalizador = Leis()
        
    def classificar(self, ementa):
        leis = self.nomalizador.get_leis(ementa)

        if len(leis) == 0:
            return (None, None)

        m = [0] * len(self.features)
        for lei in leis:
            if lei in self.features:
                i = self.features.index(lei)
                m[i] = m[i] + 1
    
        resultado = self.pipeline.predict([m])
        print(resultado)
        return (resultado[0], leis)