while True:
    n1 = int(input('Insira um número: '))
    if n1 < 0:
        break
    for cont in range(1,11):
        print(f'{n1} x {cont} = {n1 * cont}')
print('Obrigado por usar a Calculadora v3.0')