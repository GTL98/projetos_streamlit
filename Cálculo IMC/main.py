# --- Importar a biblioteca --- #
import streamlit as st
from calculo_imc import calculo_imc
from resultado_imc import resultado_imc

# --- Configurações da página --- #
st.set_page_config(page_title='Cálculo IMC', layout='centered')

# --- Adicionar o título à página --- #
st.title('Cálculo do IMC')

# --- Adicionar o campo de peso --- #
peso = st.text_input('Digite o seu peso (em Kg)')

# --- Adicionar o campo de altura --- #
altura = st.text_input('Digite a sua altura (em cm)')

# --- Criar as colunas para centralizar o botão --- #
col_1, col_2, col_3, col_4, col_5 = st.columns(5)

with col_3:
    # --- Botão do cálculo --- #
    calcular = st.button('Calcular')
    if calcular:
        # --- Calcular o IMC --- #
        if peso != '' and altura != '':
            imc = calculo_imc(peso, altura)

# --- Evitar que gere uma mensagem de erro --- #
try:
    imc = imc
except NameError:
    pass
else:
    # --- Mostrar o resultado --- #
    resultado_imc(imc)
