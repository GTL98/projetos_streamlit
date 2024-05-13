# --- Importar a biblioteca --- #
import streamlit as st


def resultado_imc(imc: float) -> str:
    """
    Função responsável por retornar o resultado o IMC.
    :param imc: Valor do IMC.
    :return: String formatada com o resultado do IMC.
    """
    # --- Comparar o valor de IMC --- #
    if imc < 18.5:
        return st.header(f'IMC: {imc:.1f} -> :blue[Magreza]')
    elif 18.5 < imc < 24.9:
        return st.header(f'IMC: {imc:.1f} -> :green[Normal]')
    elif 25 < imc < 29.9:
        return st.header(f'IMC: {imc:.1f} -> :orange[Sobrepeso]')
    elif 30 < imc < 34.9:
        return st.header(f'IMC: {imc:.1f} -> :orange[Obesidade I]')
    elif 35 < imc < 39.9:
        return st.header(f'IMC: {imc:.1f} -> :orange[Obesidade II]')
    elif imc >= 40:
        return st.header(f'IMC: {imc:.1f} -> :red[Obesidade III]')
