lista = []
while True:
    lista.append((int(input('Digite um número: '))))
    op = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Ao total foram inseridos {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Lista em Ordem Decrescente:\n{lista}')
if 5 in lista:
    print('O número 5 ESTÁ na lista!')
else:
    print('O número 5 NÃO ESTÁ na lista!')

