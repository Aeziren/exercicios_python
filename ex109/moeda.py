def moeda(num_f=0, tipo_f='€'):
    """
    Formata uma valor para padrão monetário.
    :param num_f: Valor a ser formatado.
    :param tipo_f: (Opcional, padrão Euro) Unidade monetária desejada.
    :return: O valor formatado
    """
    num = f'{tipo_f}{num_f:.2f}'.replace('.', ',')
    return num


def aumentar(valor_f=0, taxa_f=0, format_f=True):
    """
    :param valor_f: Numero que deseja aumentar.
    :param taxa_f: Porcentagem pela qual deseja aumentar.
    :param format_f: Indica se quer ou não formatação em valor monetário. (Padrão: True)
    :return: O valor acrescido da porcentagem inserida.
    """
    result = valor_f + (valor_f * taxa_f / 100)
    if format_f:
        return moeda(result)
    else:
        return result



def diminuir(valor_f=0, taxa_f=0, format_f=True):
    """
    :param valor_f: Numero que deseja diminuir.
    :param taxa_f: Porcentagem pela qual deseja diminuir.
    :param format_f: Indica se quer ou não formatação em valor monetário. (Padrão: True)
    :return: O valor reduzido pela porcentagem inserida.
    """
    result = valor_f - (valor_f * taxa_f / 100)
    if result:
        return moeda(result)
    else:
        return result


def dobro(valor_f=0, format_f=True):
    """
    :param valor_f: Valor que deseja dobrar.
    :param format_f: Indica se quer ou não formatação em valor monetário. (Padrão: True)
    :return: Dobro do valor inserido.
    """
    result = valor_f * 2
    if format_f:
        return moeda(result)
    else:
        return result


def metade(valor_f=0, format_f=True):
    """
    :param valor_f: Valor que deseja saber a metade.
    :param format_f: Indica se quer ou não formatação em valor monetário. (Padrão: True)
    :return: Metade do valor inserido.
    """
    result = valor_f / 2
    if format_f:
        return moeda(result)
    else:
        return result


