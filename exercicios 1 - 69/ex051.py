pt = int(input('Insira o primeiro termo: '))
rz = int(input('Insira a razão: '))
lista = [0]
print('Mostrando a PA: ')
for c in range(pt, pt + (rz * 15), rz):
    lista.append(c)
print(lista[1:10])
