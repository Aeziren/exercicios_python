def moeda(num_f=0, tipo_f='€'):
    """
    Formata uma valor para padrão monetário.
    :param num_f: Valor a ser formatado.
    :param tipo_f: (Opcional, padrão Euro) Unidade monetária desejada.
    :return: O valor formatado
    """
    num = f'€{num_f:.2f}'.replace('.', ',')
    return num


def aumentar(valor_f=0, taxa_f=0):
    """
    :param valor_f: Numero que deseja aumentar.
    :param taxa_f: Porcentagem pela qual deseja aumentar.
    :return: O valor acrescido da porcentagem inserida.
    """
    result = valor_f + (valor_f * taxa_f / 100)
    return result


def diminuir(valor_f=0, taxa_f=0):
    """
    :param valor_f: Numero que deseja diminuir.
    :param taxa_f: Porcentagem pela qual deseja diminuir.
    :return: O valor reduzido pela porcentagem inserida.
    """
    result = valor_f - (valor_f * taxa_f / 100)
    return result


def dobro(valor_f=0):
    """
    :param valor_f: Valor que deseja dobrar.
    :return: Dobro do valor inserido.
    """
    return valor_f * 2


def metade(valor_f=0):
    """
    :param valor_f: Valor que deseja saber a metade.
    :return: Metade do valor inserido.
    """
    return valor_f / 2
