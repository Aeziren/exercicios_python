r1 = float(input('Primeira Reta: '))
r2 = float(input('Segunda Reta: '))
r3 = float(input('Terceira Reta: '))
lista = [r1, r2, r3]
lista.sort()
if lista[0] + lista[1] > lista[2]:
    print('PODE se formar um triângulo!')
else:
    print('NÃO PODE se formar um triângulo!')

