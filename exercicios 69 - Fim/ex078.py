lista = []
for n in range(0, 5):
    lista.append(int(input(f'Valor {n + 1}: ')))
maior = max(lista)
menor = min(lista)
print(f'O maior valor é: {maior} nas posições:', end=' ')
for pos in range(0, len(lista)):
    if lista[pos] == maior:
        print(f'{pos + 1} ', end='')
print(f'\nO menor valor é: {menor} nas posições:', end=' ')
for pos in range(0, len(lista)):
    if lista[pos] == menor:
        print(f'{pos + 1} ', end='')
