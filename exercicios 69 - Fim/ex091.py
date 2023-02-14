from random import randint
from operator import itemgetter
ranking = []
result = {}
ordem = []
for c in range(1, 5):
    result[f'Jogador {c}'] = randint(1, 6)
for k, v in result.items():
    print(f'{k} tirou: {v}')
print(f'{" RANKING ":=^24}')
ranking = sorted(result.items(), key=itemgetter(1), reverse=True)
for c, p in enumerate(ranking):
    print(f'{c + 1}º Lugar: {p[0]} tirou {p[1]}')
