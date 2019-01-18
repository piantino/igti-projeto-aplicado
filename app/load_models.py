
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.externals import joblib

import os

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
MODELOS_FOLDER = os.path.join(PROJECT_ROOT, 'modelos')

class Loader(object):
    def load_model(self, file):
        return joblib.load(os.path.join(MODELOS_FOLDER, file))
    
    def get_pipelines(self, rotulos):
        pipelines = []

        dense = FunctionTransformer(lambda x: x.todense(), accept_sparse=True, validate=True)

        for rotulo in rotulos:
            vect = self.load_model('CountVectorizer-' + rotulo + '.pkl')
            tfidf = self.load_model('TfidfTransformer-' + rotulo + '.pkl')
            clf = self.load_model('Modelo-' + rotulo + '.pkl') 
            p = Pipeline([
                ('vect', vect),
                ('tfidf', tfidf),
                ('dense', dense),
                ('clf', clf)
            ])
            pipelines.append(p)
        return pipelines