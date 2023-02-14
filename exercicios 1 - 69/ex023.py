num = int(input('Insira um número inteiro (0 a 9999): '))
un = num // 1 % 10
dz = num // 10 % 10
ct = num // 100 % 10
ml = num // 1000 % 10
print('Analisando...')
print('{} Unidades'.format(un))
print('{} Dezenas'.format(dz))
print('{} Centenas'.format(ct))
print('{} Milhares'.format(ml))

