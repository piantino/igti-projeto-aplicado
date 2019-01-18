import requests
from bs4 import BeautifulSoup
from bs4.element import Comment

class Crawler(object):
    def __init__(self):
        self.browser = requests.Session()
        
    def get_acordaos(self, num_proc):
        url = "http://busca.tjsc.jus.br/jurisprudencia/buscaajax.do?&nuProcesso=" + num_proc +"&categoria=acordaos&q=&only_ementa=&qualquer=&excluir=&prox1=&prox2=&proxc=&frase=&classe=&juizProlator=&origem=&relator=&radio_campo=ementa&faceta=true&busca=avancada&datainicial=&datafinal=&ps=20&sort=dtJulgamento+desc"

        r = self.browser.get(url)

        soup = BeautifulSoup(r.text, 'html.parser')
        resultados = soup.find_all('div', class_="resultados")

        acordaos = []
        for resultado in resultados:
            acordao = {
                "texto": resultado.p.get_text().strip().replace('\n\n', '\n'),
                "ementa": resultado.find_all('textarea')[0].find_all(text=True)[0].strip()
            }

            acordaos.append(acordao)
        return acordaos


if __name__ == "__main__":
    crawler = Crawler()
    acordaos = crawler.get_acordaos('0003960-47.2013.8.24.0039')

    for acordao in acordaos:
        print(acordao['texto'])
        print(acordao['ementa'])