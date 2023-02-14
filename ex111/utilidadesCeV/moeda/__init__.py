def moeda(num_f=0, tipo_f='€'):
    """
    Formata uma valor para padrão monetário.
    :param num_f: Valor a ser formatado.
    :param tipo_f: (Opcional, padrão Euro) Unidade monetária desejada.
    :return: O valor formatado
    """
    num = f'{tipo_f}{num_f:.2f}'.replace('.', ',')
    return num


def aumentar(valor_f=0, taxa_f=0, formt_f=False):
    """
    :param valor_f: Numero que deseja aumentar.
    :param taxa_f: Porcentagem pela qual deseja aumentar.
    :param formt_f: Indica se quer ou não formatação em valor monetário. (Padrão: False)
    :return: O valor acrescido da porcentagem inserida.
    """
    result = valor_f + (valor_f * taxa_f / 100)
    if formt_f:
        return moeda(result)
    else:
        return result


def diminuir(valor_f=0, taxa_f=0, formt_f=False):
    """
    :param valor_f: Numero que deseja diminuir.
    :param taxa_f: Porcentagem pela qual deseja diminuir.
    :param formt_f: Indica se quer ou não formatação em valor monetário. (Padrão: False)
    :return: O valor reduzido pela porcentagem inserida.
    """
    result = valor_f - (valor_f * taxa_f / 100)
    if formt_f:
        return moeda(result)
    else:
        return result


def dobro(valor_f=0, formt_f=False):
    """
    :param valor_f: Valor que deseja dobrar.
    :param formt_f: Indica se quer ou não formatação em valor monetário. (Padrão: False)
    :return: Dobro do valor inserido.
    """
    result = valor_f * 2
    if formt_f:
        return moeda(result)
    else:
        return result


def metade(valor_f=0, formt_f=False):
    """
    :param valor_f: Valor que deseja saber a metade.
    :param formt_f: Indica se quer ou não formatação em valor monetário. (Padrão: False)
    :return: Metade do valor inserido.
    """
    result = valor_f / 2
    if formt_f:
        return moeda(result)
    else:
        return result


def resumo(num_f=0, acrescimo_f=0, desconto_f=0, formt_f=False):
    print('=' * 30, f'\n{f"Exibindo dados do valor {num_f}":^30}')
    print('=' * 30)
    print(f'Dobro: {dobro(num_f, formt_f)}')
    print(f'Metade: {metade(num_f, formt_f)}')
    print(f'Com aumento de {acrescimo_f}%: {aumentar(num_f, acrescimo_f, formt_f)}')
    print(f'Com desconto de {desconto_f}%: {diminuir(num_f, desconto_f, formt_f)}')
    print('=' * 30)
