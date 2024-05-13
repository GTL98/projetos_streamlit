# --- Importar a biblioteca --- #
import requests


def pegar_cotacoes(moeda: str) -> tuple:
    """
    Função responsável por pegar as cotações das moedas.
    :param moeda: Moeda para a conversão
    :return: Tupla com as informações da cotação em tempo real.
    """
    # --- Obter a requisição --- #
    requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

    # --- Obter o dicionário da requisição --- #
    dic_requisicao = requisicao.json()

    if moeda == 'Dólar':
        dolar = dic_requisicao['USDBRL']['bid']
        maximo = dic_requisicao['USDBRL']['high']
        minimo = dic_requisicao['USDBRL']['low']
        return dolar, maximo, minimo

    elif moeda == 'Euro':
        euro = dic_requisicao['EURBRL']['bid']
        maximo = dic_requisicao['EURBRL']['high']
        minimo = dic_requisicao['EURBRL']['low']
        return euro, maximo, minimo

    elif moeda == 'BitCoin':
        bitcoin = dic_requisicao['BTCBRL']['bid']
        maximo = dic_requisicao['BTCBRL']['high']
        minimo = dic_requisicao['BTCBRL']['low']
        return bitcoin, maximo, minimo
