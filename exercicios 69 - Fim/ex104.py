def leiaInt(texto):
    """
    -> Função para aceitar apenas números. Converte qualquer tipo de dado
    para int
    :param texto: Texto de input
    :return: Retorna o número inserido pelo usuario no formato inteiro.
    """
    num_f = str(input(f'{texto}'))
    while True:
        if num_f.isnumeric():
            num_f = int(num_f)
            break
        print('\033[0;31mInválido. Digite apenas números!\033[m')
        num_f = str(input(f'{texto}'))
    return num_f


n1 = leiaInt('Digite um número: ')
print(f'Você digitou o número {n1}.')


