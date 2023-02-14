from datetime import date
maior = int(0)
menor = int(0)
ano = date.today().year
for c in range(1, 8):
    nasc = int(input('Ano de Nascimento Pessoa {}: '.format(c)))
    if ano - nasc >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('MAIORES DE IDADE: {}\nMENORES DE IDADE: {}'.format(maior, menor))
