r1 = float(input('Primeira Reta: '))
r2 = float(input('Segunda Reta: '))
r3 = float(input('Terceira Reta: '))
if r1 == r2 and r1 == r3:
    tri = str('Equilátero')
elif r1 == r2 or r1 == r3 or r3 == r2:
    tri = str('Isosceles')
else:
    tri = str('Escaleno')
lista = [r1, r2, r3]
lista.sort()
if lista[0] + lista[1] > lista[2]:
    print('Com esse valores forma-se um Triângulo {}'.format(tri))
else:
    print('Impossível formar um Triângulo com esses valores!')
