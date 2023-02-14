def ficha(nome_f, gols_f):
    if not nome_f:
        nome_f = '<desconhecido>'
    if gols_f.isnumeric():
        gols_f = int(gols_f)
    else:
        gols_f = 0
    print(f'O jogador {nome_f} fez {gols_f} gols.')


nome = str(input('Nome do jogador: ')).strip()
gols_str = str(input('Gols marcados: ')).strip()
ficha(nome, gols_str)


