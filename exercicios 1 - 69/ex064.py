print('Insira quantos valores quiser!\n[ 999 ] para Parar')
qtd_valores = result = 0
n1 = int(input('Valor {}: '.format(qtd_valores + 1)))
while n1 != 999:
    result += n1
    qtd_valores += 1
    n1 = int(input('Valor {}: '.format(qtd_valores + 1)))
print('Você inseriu {} números!\nA soma entre eles é: {}'.format(qtd_valores, result))
