# Projeto: Classificação de processos para distribuição entre assessores.

> Aluno: [Andre Porto Leal Piantino](http://andrepiantino.com.br)<br>
> Insituição: [IGTI - Instituto de Gestão e Tecnologia da Informação](https://www.igti.com.br)<br>
> Curso: [MBA em Aprendizado de Máquina](https://www.igti.com.br/cursos/mba-em-aprendizado-de-maquina/) - AMQ181A<br>
> Linha de Especialização: Machine Learning Aplicado ao Processamento de Textos<br>
> Orientador: Professor Rafael Albergaria Carmo

## O problema


3ª vice presidência do Tribunal de Santa Catarina

---

## A proposta de solução

---

## Os dados

A base dados de acórdãos conta com mais de 200 mil ementas, para esse trabalho foram selecionados apenas as ementas de processos que podem tramitar na 3ª vice presidência, totalizando mais de **111.361???** registros .<br>
Os dados foram coletados no dia **31/10/2018**.

#NOTEBOOK: [analise_coleta.ipynb](notebooks/analise_coleta.ipynb)

---

### Fonte de dados

A ementas são **públicas** e podem ser acessadas na [Busca de Jurisprudência Catarinense](http://busca.tjsc.jus.br/jurisprudencia/).

---

### Estrutura


---

## Rótulos


Existem duas fontes de rótulos, ou seja processos já classificados. Uma delas é obtida da Base do Sistema SAJ a qual é alimentada pelos estagiários (especialistas júniors) e pelos assessores (especialistas), denominado "rótulos manuais". A outra provém de um script que busca frases expecíficas, desenvolvido por [Luís Felipe Kuhn Göcks](https://www.linkedin.com/in/lu%C3%ADs-felipe-kuhn-g%C3%B6cks-9a9874153/) e [Glauber Machado Pinto](https://www.linkedin.com/in/glauber-machado-pinto/), denominada "rótulos script".

### Tipos de rótulos



---

## Pré-processamento

---

## Aprendizado de modelos


supervisionado

---
## Avaliação e comparação de modelos


---
## Conclusão
---

## Executando o projeto

cd ./docker
docker-composer up
