import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return "A API está no ar"

@app.route('/pegarvendas')
def pegar_vendas():
    tabela = pd.read_csv('resources/advertising.csv')

    total_vendas  = tabela["Vendas"].sum()
    
    resposta = {"total_vendas": total_vendas}

    return jsonify(resposta)


if __name__ == '__main__':
    app.run()