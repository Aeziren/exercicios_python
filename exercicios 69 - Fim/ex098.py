from time import sleep


def contador(inicio_f, fim_f, passo_f):
    if inicio_f > fim_f:
        if passo_f > 0:
            passo_f = passo_f * -1
        fim_f -= 1
    else:
        fim_f += 1
    for c in range(inicio_f, fim_f, passo_f):
        print(f'{c} ', end='')
        sleep(0.3)


contador(1, 11, 1)
print('...Fim!')
contador(10, -1, -2)
print('...Fim!')
inicio = int(input('\nInicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
