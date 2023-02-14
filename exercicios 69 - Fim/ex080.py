lista = []
for c1 in range(0, 5):
    num = int(input(f'Valor {c1}: '))
    if c1 == 0 or num > lista[-1]:
        lista.append(num)
        print(f'Número {num} adicionado ao fim da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Número {num} adicionado à posição {pos} da lista.')
                break
            pos += 1
print(lista)
