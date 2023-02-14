print('Calcular PA:')
pm = int(input('Primeiro Termo: '))
rz = int(input('Razão: '))
cont = 0
meta = 10
print('[', end='')
while cont < meta:
    print('{}, '.format(pm), end='')
    pm = pm + rz
    cont = cont + 1
    if cont == meta:
        print('...]'.format(pm))
        print('Deseja mostrar mais resultados?')
        meta = int(input('Insira o valor ou [ 0 ] para finalizar: '))
        meta = meta + cont
print('Foram exibidos {} resultados!\nObrigado, volte sempre!'.format(meta))

