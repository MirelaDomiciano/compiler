# Projeto Compiler

Este projeto é um trabalho da matéria de compiladores que tem por objetivo implementar um analisador léxico e um analisador sintático para a linguagem de programação CêPy. A linguagem em questão foi desenvolvida com usando como base tanto a linguagem C quanto a linguagem Python e também adicionando algumas partes autênticas. O projeto se trata de um compilador simples desenvolvido em Python, utilizando as bibliotecas `ply.lex` e `ply.yacc` para análise léxica e sintática, respectivamente. O projeto é dividido em três componentes principais: `lexer`, `myParser`, e `myTranslator`.

## Componentes

### Lexer (`lexer.py`)

O componente `lexer` é responsável pela análise léxica do código-fonte. A biblioteca `ply.lex` é utilizada para definir os tokens da linguagem e as regras para a análise léxica. Tokens são especificados através de expressões regulares, e a biblioteca gera um analisador léxico que pode identificar esses tokens no código-fonte. No lexer são definidos os elementos básicos da linguagem, como palavras-chave, identificadores, operadores, etc. 

### Parser (`myParser.py`)

O `myParser` é o componente que realiza a análise sintática. Ele constrói a árvore sintática do programa a partir dos tokens identificados pelo lexer. Utiliza a biblioteca `ply.yacc` permite especificar a gramática de forma declarativa, usando docstrings Python para definir as regras de produção. A biblioteca gera um parser que pode construir a árvore sintática do programa com base na gramática definida. O parser também define a precedência dos operadores para resolver ambiguidades na gramática.

### Translator (`myTranslator.py`)

O `myTranslator` é responsável por traduzir a árvore sintática gerada pelo parser em código Python. Este componente implementa a lógica de tradução, visitando cada nó da árvore sintática e gerando o código correspondente em Python.

## Instalações

###Python
Instalação oficial: [documentação oficial do Python](https://python.org.br/instalacao-windows/).

### ply.lex e ply.yacc
Para utilização dessas ferramentas é necessários instalar a biblioteca ply, pode-se usar o comando abaixo:
[`pip install ply`]

## Como Executar

Com essas dependências instaladas já é possível rodar o programa. Para isso execute o programa myParser.py:
[`python3 myParser.py`]

## Output do programa 
Como output o programa gera um arquivo .txt na pasta files_txt para cada exemplo presente na pasta src. Esse arquivo contem a descrição dos comandos de cada um dos exemplos. Além disso, também é gerado um arquivo .py para na pasta files_py para cada um dos exemplos, esses arquivos são a tradução dos exemplos para a linguagem Python. Esses arquivos somente são gerados para os exemplos que contém a extensão .cpa, que é a extensão para os arquivos da nossa linguagem CPython. 


