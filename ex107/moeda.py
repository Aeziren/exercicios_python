def aumentar(valor_f, taxa_f):
    """
    :param valor_f: Numero que deseja aumentar.
    :param taxa_f: Porcentagem pela qual deseja aumentar.
    :return: O valor acrescido da porcentagem inserida.
    """
    result = valor_f + (valor_f * taxa_f / 100)
    return result


def diminuir(valor_f, taxa_f):
    """
    :param valor_f: Numero que deseja diminuir.
    :param taxa_f: Porcentagem pela qual deseja diminuir.
    :return: O valor reduzido pela porcentagem inserida.
    """
    result = valor_f - (valor_f * taxa_f / 100)
    return result


def dobro(valor_f):
    """
    :param valor_f: Valor que deseja dobrar.
    :return: Dobro do valor inserido.
    """
    return valor_f * 2


def metade(valor_f):
    """
    :param valor_f: Valor que deseja saber a metade.
    :return: Metade do valor inserido.
    """
    return valor_f / 2
