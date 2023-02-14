def fatorial(num_f=0, mostra=False):
    """
    :param num_f: Numero a ser calculado fatorial
    :param mostra: True ou False - Exibe o cálculo
    :return: Nenhum
    """
    total = 1
    if not mostra:
        for c in range(num_f, 0, -1):
            total = total * c
        print(total)
    else:
        for c in range(num_f, 0, -1):
            total = total * c
            if c > 1:
                print(f'{c} x', end=' ')
            else:
                print(f'{c} =', end=' ')
        print(total)


n1 = int(input('Quer ver o fatorial de: '))
op = str(input('Ver processo? [S/N] ')).strip().upper()[0]
if op in 'S':
    op = True
else:
    op = False
fatorial(n1, mostra=op)
help(fatorial)
