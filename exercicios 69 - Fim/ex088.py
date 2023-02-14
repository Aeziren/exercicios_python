from random import randint
from time import sleep
c = int(input('Quantos jogos deseja gerar? '))
jogo = []
lista = []
num = 0
for c1 in range(0, c):
    for c2 in range(0, 6):
        num = randint(1, 60)
        while num in jogo:
            num = randint(1, 60)
        jogo.append(num)
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()
for c, j in enumerate(lista):
    sleep(1)
    print(f'Jogo {c + 1}: {j}')
