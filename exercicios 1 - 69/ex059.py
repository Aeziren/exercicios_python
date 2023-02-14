n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
op = 0
while op != 5:
    print('=-' * 15, '''\n[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior valor
[ 4 ] Inserir novos números
[ 5 ] Sair do programa\n''', '=-' * 15)
    op = int(input('Opção: '))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 == n2:
            print('Valores Iguais!')
        elif n1 > n2:
            print('O maior valor é: {}'.format(n1))
        else:
            print('O maior valor é: {}'.format(n2))
    elif op == 4:
        n1 = int(input('Valor 1: '))
        n2 = int(input('Valor 2: '))
    elif op == 5:
        print('Obrigado por usar o programa.')
    else:
        print('Digite um número válido!')
