aluno = []
notas = []
lista = []
cont = media = 0
op = ' '
while True:
    aluno.append(str(input(f'Aluno {cont}: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    cont += 1
    aluno.append(notas[:])
    lista.append((aluno[:]))
    aluno.clear()
    notas.clear()
    op = str(input('Continuar? [S/N]')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Continuar? [S/N]')).strip().upper()[0]
    if op in 'N':
        break
print(f'{" Resultados ":=^30}')
print('Nº', f'{"Nome":^14}', 'Média')
for c in range(0, len(lista)):
    print(c, end=' ')
    print(f'{lista[c][0]:.<15}', end=' ')
    media = (lista[c][1][0] + lista[c][1][1]) / 2
    print(media)
print('=' * 30)
print('[ 999 ] Para PARAR')
while True:
    op = int(input('Digite o número do aluno que deseja ver as notas: '))
    if op == 999:
        break
    print(lista[op][1])
