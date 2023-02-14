dados = {}
todos = []
media_idade = 0
while True:
    dados['arq'] = str(input('Nome: ')).strip().title()
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    media_idade += dados['idade']
    todos.append(dados.copy())
    op = str(input('Continuar? [S/N] ')).strip().upper()[0]
    dados.clear()
    while op not in 'SN':
        op = str(input('Continuar? [S/N]')).strip().upper()[0]
    if op in 'N':
        media_idade = media_idade / len(todos)
        break
print('=' * 30)
print(f'Pessoas cadastradas: {len(todos)}')
print(f'Media de idade: {media_idade:.2f}')
print('Pessoas acima da média de idade:')
for p in todos:
    if p['idade'] > media_idade:
        print(f'  -{p["arq"]}')
print('Mulheres na lista:')
for p in todos:
    if p['sexo'] in 'F':
        print(f'  -{p["arq"]}')
