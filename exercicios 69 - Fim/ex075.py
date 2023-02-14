lista = (int(input('Valor 1: ')),
         int(input('Valor 2: ')),
         int(input('Valor 3: ')),
         int(input('Valor 4: ')))

print(f'Vezes em que o número 9 apareceu: {lista.count(9)}')
if lista.count(3) == True:
    print(f'O número 3 apareceu pela primeira vez na posição: {lista.index(3) + 1}')
print('Os números pares foram: ', end='')
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        print(f'{lista[c]} ', end='')
