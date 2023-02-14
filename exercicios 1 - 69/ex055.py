maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input('Qual o peso da {}ª dados: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso inserido foi: {}\nO menor peso inserido foi: {}'.format(maior, menor))