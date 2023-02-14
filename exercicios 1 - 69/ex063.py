print('Sequencia de Fibonacci')
meta = int(input('Quantos elementos quer mostrar? '))
meta = meta - 2
lista = [0, 1]
c = p1l = 0
p2l = 1
while c < meta:
    result = lista[p1l] + lista [p2l]
    lista.append(result)
    p1l += 1
    p2l += 1
    c += 1
print(lista)
