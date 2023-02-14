from ex108 import moeda


num = float(input('Valor €: '))
print(f'O dobro de {moeda.moeda(num)} é: {moeda.moeda(moeda.dobro(num))}')
print(f'Metade de {moeda.moeda(num)} é: {moeda.moeda(moeda.metade(num))}')
print(f'{moeda.moeda(num)} com acréscimo de 15% é: {moeda.moeda(moeda.aumentar(num, 15))}')
print(f'{moeda.moeda(num)} com desconto de 7% é: {moeda.moeda(moeda.diminuir(num, 7))}')
