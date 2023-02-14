grupo = []
dados = []
maiorpeso = menorpeso = 0
while True:
    dados.clear()
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(grupo) == 0:
        maiorpeso = dados[1]
        menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    grupo.append(dados[:])
    op = str(input('Continuar? [S/N]')).strip().title()[0]
    while op not in 'SN':
        op = str(input('Continuar? [S/N]')).strip().title()[0]
    if op in 'N':
        break
print(f'Foram cadastradas {len(grupo)} pessoas.')
print(f'As pessoas mais pesadas, com {maiorpeso}KGs são: ', end=' ')
for c in range(0, len(grupo)):
    if grupo[c][1] == maiorpeso:
        print(f'{grupo[c][0]}...', end=' ')
print(f'\nAs pessoas mais magras, com {menorpeso}KGs são: ', end=' ')
for c in range(0, len(grupo)):
    if grupo[c][1] == menorpeso:
        print(f'{grupo[c][0]}...', end=' ')
