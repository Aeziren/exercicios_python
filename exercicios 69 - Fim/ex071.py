valor = int(input('Informe quanto quer sacar: €'))
n50 = n20 = n10 = n1 = 0
while valor >= 50:
    valor -= 50
    n50 += 1
while valor >= 20:
    valor -= 20
    n20 += 1
while valor >= 10:
    valor -= 10
    n10 += 1
while valor >= 1:
    valor -= 1
    n1 += 1
print('=' * 30, '\nLIBERANDO NOTAS: ')
print(f'Notas de €50: {n50}\nNotas de €20: {n20}')
print(f'Notas de €10: {n10}\nNotas de €1: {n1}')
