# --- Importar a biblioteca --- #
import streamlit as st


def tabela_cotacao(moeda: str, cotacao: str, maximo: str, minimo: str) -> None:
    """
    Função responsável por criar a tabela com as informações da cotação.
    :param moeda: Moeda para a cotação.
    :param cotacao: Cotação em tempo real da moeda.
    :param maximo: Máximo do dia da moeda.
    :param minimo: Mínimo do dia da moeda.
    :return: Tabela com as informações
    """
    # --- Tratar os valores da cotação --- #
    if '.' in cotacao:
        cotacao = cotacao[:4]
    if '.' in maximo:
        maximo = maximo[:4]
    if '.' in minimo:
        minimo = minimo[:4]

    # --- Configurações da tabela --- #
    st.write(
        '''
        <style>
        table, th, td {
            font-size: 20px
            }
        </style>
        ''',
        unsafe_allow_html=True
    )

    # --- Escrever a tabela --- #
    st.write(
        f'''
        <table>
            <tr>
                <th>Moeda</th>
                <th>Cotação</th>
                <th>Máximo</th>
                <th>Mínimo</th>
            </tr>
            <tr>
                <td>{moeda}</td>
                <td>R$ {cotacao}</td>
                <td>R$ {maximo}</td>
                <td>R$ {minimo}</td>
            </tr>
        </table>
''',
        unsafe_allow_html=True
    )
