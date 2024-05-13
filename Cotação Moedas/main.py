# --- Importar as bibliotecas --- #
import streamlit as st
from pegar_cotacoes import pegar_cotacoes
from tabela_cotacoes import tabela_cotacao

# --- Configuraçõe da página --- #
st.set_page_config(page_title='Cotação Moedas', layout='centered')

# --- Título da página --- #
st.title('Cotação Moedas')

# --- Caixa de seleção para escolher a moeda --- #
moedas = ['Dólar', 'Euro', 'BitCoin']
moeda = st.selectbox(
    label='Moedas',
    options=moedas,
    placeholder='Selecione uma moeda',
    index=None
)

# --- Colunas para centralizar o botão --- #
col_1, col_2, col_3, col_4, col_5 = st.columns(5)
with col_3:
    # --- Botão da cotação --- #
    botao_cotacao = st.button('Cotação')

    # --- Resultado da cotação --- #
    if botao_cotacao:
        cotacao = pegar_cotacoes(moeda)

try:
    cotacao = cotacao
except NameError:
    pass
else:
    tabela_cotacao(moeda, cotacao[0], cotacao[1], cotacao[2])
