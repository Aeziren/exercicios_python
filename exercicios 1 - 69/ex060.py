cont = int(input('Digite um número para saber seu fatorial: '))
result = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont != 1 else ' = ', end='')
    result = result * cont
    cont -= 1
print('{}'.format(result))
