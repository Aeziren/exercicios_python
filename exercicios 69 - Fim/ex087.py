matriz = [[], [], []]
crtl = pont = 0
pares = soma_3_col = maior_2_lin = 0
while True:
    matriz[crtl].append(int(input(f'Valor de [{crtl}, {pont}]: ')))
    if matriz[crtl][-1] % 2 == 0:
        pares += matriz[crtl][-1]
    if pont == 2:
        soma_3_col += matriz[crtl][-1]
    if crtl == 1:
        if matriz[1][-1] > maior_2_lin:
            maior_2_lin = matriz[1][-1]
    if crtl == 2 and pont == 2:
        break
    if pont == 2:
        print('...')
        crtl += 1
        pont = -1
    pont += 1
crtl = pont = 0
print('=-' * 14)
while True:
    print(f'[ {matriz[crtl][pont]:^3} ]   ', end=' ')
    if crtl == 2 and pont == 2:
        print()
        break
    if pont == 2:
        print('\n')
        crtl += 1
        pont = -1
    pont += 1
print('=-' * 14)
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores na 3º coluna é: {soma_3_col}')
print(f'O maior valor da 2ª linha é: {maior_2_lin}')