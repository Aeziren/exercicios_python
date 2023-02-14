cont = 0
lista = []
while True:
    num = int(input(f'Valor {cont}: '))
    if num not in lista:
        lista.append(num)
        print(f'Adicionando {num} a lista...')
    else:
        print(f'O número {num} já está na lista.')
    op = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if op == 'N':
        break
    print(lista)
    cont += 1
print('=' * 30)
print(sorted(lista))
