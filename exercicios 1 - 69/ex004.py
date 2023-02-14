var1 = input('Digite algo: ')
print('{} é uma variável da {}'.format(var1, type(var1)))
print('É um número? {}'.format(var1.isnumeric()))
print('É alfabético? {}'.format(var1.isalpha()))
print('É alfanumérico? {}'.format(var1.isalnum()))
print('Ou é apenas um espaço? {}'.format(var1.isspace()))

