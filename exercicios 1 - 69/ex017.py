from math import hypot
ca = float(input('Insira o cateto adjacente: '))
co = float(input('Agora o cateto oposto:'))
# print('Num triângulo retangulo com cateto oposto {} e cateto adjacente medindo {} a hipotenusa é igual a {:.2f}'.format(co, ca, (co ** 2 + ca ** 2) ** 0.5))
print('Num triângulo retângulo com cateto oposto {} e cateto adjacente medindo {} a hipotenusa é igual a {:.2f}'.format(co, ca, hypot(co, ca)))


