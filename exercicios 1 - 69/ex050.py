soma = 0
contpar = 0
for c in range(1, 7):
    n1 = int(input('Numero inteiro {}: '.format(c)))
    if n1 % 2 == 0:
        contpar = contpar + 1
        soma = soma + n1
print('A soma dos {} números pares é: {}'.format(contpar, soma))
