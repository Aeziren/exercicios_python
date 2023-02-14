lista = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athlético PR', 'Atlético MG',
         'Fortaleza', 'São Paulo', 'América MG', 'Botafogo', 'Santos', 'Goiás', 'RedBull Bragantino', 'Coritiba',
         'Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(f'Os 5 primeiros colocados são: {lista[:5]}')
print(f'Os 4 últimos colocados são: {lista[:15:-1]}')
print(f'A lista em ordem alfabética é: {sorted(lista)}')
print(f'O time do Flamengo está na {lista.index("Flamengo") + 1}ª posição')

