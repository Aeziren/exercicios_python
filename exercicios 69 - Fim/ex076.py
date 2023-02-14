lista = ('Martelo', 3.5, 'Fita Métrica', 2.39, 'Chave de Boca', 4, 'Chave Inglesa', 6.99, 'Compressor', 470.99,
         'Multímetro', 12.50, 'Chave Roquete', 9.99, 'Pé de Cabra', 7.89, 'Chave Phillips', 3.80)
print('{}'.format('-' * 42), '\n{:^42}'.format('Listagem de Preços:'), '\n{}'.format('-' * 42))
for c in range(0, len(lista), 2):
    print('{:.<30}{:<3}{:>8.2f}'.format(lista[c], '€', lista[c + 1]))
print('-' * 42)
