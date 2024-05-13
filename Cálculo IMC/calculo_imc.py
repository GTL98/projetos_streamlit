def calculo_imc(peso: str, altura: str) -> float:
    """
    Função responsável por calcular o IMC.
    :param peso: Peso da pessoa (em Kg).
    :param altura: Altura de pessoa (em cm).
    :return: IMC calculádo.
    """
    # --- Conveter o peso de str para float --- #
    peso = float(peso.replace(',', '.'))

    # --- Converter a altura de str para float --- #
    altura = int(altura) / 100

    # --- Calcular o IMC --- #
    imc = peso / (pow(altura, 2))

    return imc
