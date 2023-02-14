matriz = [[], [], []]
crtl = pont = 0
while True:
    matriz[crtl].append(int(input(f'Valor de [{crtl}, {pont}]: ')))
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





