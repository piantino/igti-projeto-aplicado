
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import FunctionTransformer

from sklearn.externals import joblib

class Loader(object):
    def load_model(self, file):
        return joblib.load(file)
    
    def get_pipelines(self, rotulos):
        pipelines = []

        dense = FunctionTransformer(lambda x: x.todense(), accept_sparse=True, validate=True)

        for rotulo in rotulos:
            vect = self.load_model('../modelos/CountVectorizer-' + rotulo + '.pkl')
            tfidf = self.load_model('../modelos/TfidfTransformer-' + rotulo + '.pkl')
            clf = self.load_model('../modelos/Modelo-' + rotulo + '.pkl') 
            p = Pipeline([
                ('vect', vect),
                ('tfidf', tfidf),
                ('dense', dense),
                ('clf', clf)
            ])
            pipelines.append(p)
        return pipelines