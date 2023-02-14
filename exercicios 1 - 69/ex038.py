n1 = int(input('Primeiro número: '))
n2 = int(input('Primeiro número: '))
if n1 > n2:
    print('O primeiro número ({}) é maior que o segundo ({})!'.format(n1, n2))
elif n2 > n1:
    print('O segundo número ({}) é maior que o primeiro ({})!'.format(n2, n1))
else:
    print('Os números são iguais!')