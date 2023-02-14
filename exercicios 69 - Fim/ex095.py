dados = dict()
todos = list()
while True:
    dados['arq'] = str(input('Nome: ')).strip().title()
    dados['jogos'] = int(input('Partidas Jogadas: '))
    dados['total de gols'] = 0
    for c in range(1, dados['jogos'] + 1):
        dados[f'partida {c}'] = int(input(f'Gols na Partida {c}: '))
        dados['total de gols'] += dados[f'partida {c}']
    todos.append(dados.copy())
    op = str(input('Continuar? [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        print('Opção inválida!')
        op = str(input('Continuar? [S/N]')).strip().upper()[0]
    if op in 'N':
        break
print(f'{" Tabela: ":=^30}')
print(f'{"ID":<4} {"Nome":<20} {"PTDs":^5} {"Gols":^7}')
for cont, jog in enumerate(todos):
    print(f'{cont:<4}{jog["arq"]:.<20} {jog["jogos"]:^5} {jog["total de gols"]:^7}')
print('Digite "999" para encerrar.')
while True:
    op = int(input('ID do jogador que deseja ver detalhes: '))
    if op == 999:
        break
    for cont in range(0, todos[op]['jogos']):
        print(f'Partida {cont}: {todos[op][f"partida {cont + 1}"]} gols')
