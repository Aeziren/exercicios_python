from ex107 import moeda


num = float(input('Valor €: '))
print(f'O dobro de {num} é: {moeda.dobro(num)}')
print(f'Metade de {num} é: {moeda.metade(num)}')
print(f'{num} com acréscimo de 15% é: {moeda.aumentar(num, 15)}')
print(f'{num} com desconto de 7% é: {moeda.diminuir(num, 7)}')