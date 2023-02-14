homens = mulher_20 = maior18 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if idade >= 18:
        maior18 += 1
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    op = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-' * 35)
    if op in 'N':
        break
print('=' * 30, '\nEXIBINDO RESULTADOS:')
print(f'Maiores de 18: {maior18}\nTotal de homens: {homens}\nMulheres abaixo de 20 anos: {mulher_20}')
