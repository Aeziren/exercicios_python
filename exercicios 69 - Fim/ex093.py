dados = dict()
gols = 0
dados['arq'] = str(input('Nome: ')).strip().title()
dados['jogos'] = int(input('Partida Jogadas: '))
for c in range(1, dados['jogos'] + 1):
    dados[f'partida {c}'] = int(input(f'Gols na partida {c}: '.title()))
    gols += dados[f'partida {c}']
dados['total de gols'] = gols
print(f'{" RESULTADOS ":=^30}')
for k, v in dados.items():
    print(f'{k}: {v}'.title())
