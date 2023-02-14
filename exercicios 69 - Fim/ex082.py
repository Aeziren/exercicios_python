numeros = []
par = []
impar = []
while True:
    numeros.append(int(input('Insira um valor: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Continuar? [S/N] ')).strip().upper()[0]
    if op in 'N':
        break
for x in numeros:
    if x % 2 == 0:
        print('teste')
        par.append(x)
    else:
        impar.append(x)
print(f'Lista Original: {numeros}\nPares: {par}\nImpares: {impar}')