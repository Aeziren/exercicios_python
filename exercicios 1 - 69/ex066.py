print('Calculadora de Soma:\nDigite [999] para sair.')
cont = soma = 0
while True:
    n1 = int(input(f'Valor {cont + 1}: '))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print(f'Você inseriu {cont} valores.\nA soma deles é igual a: {soma}')

