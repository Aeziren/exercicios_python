from random import randint


def sorteia():
    lista = list()
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print(f'A lista gerada foi: {lista}')
    return lista


def soma_par(lista_f):
    total = 0
    for n in lista_f:
        if n % 2 == 0:
            total += n
    print(f'A soma dos números na lista é: {total}')


soma_par(sorteia())
