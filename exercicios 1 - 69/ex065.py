n1 = int(input('Digite um número: '))
maior = menor = soma = n1
op = 'S'
cont = 1
while op in 'S':
    op = '0'
    while op not in 'SN':
        op = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if op == 'S':
            cont += 1
            n1 = int(input('Digite outro número: '))
            soma += n1
            if n1 > maior:
                maior = n1
            elif n1 < menor:
                menor = n1
        if op not in 'SN':
            print('Opção inválida! Tente novamente.\n')
if cont > 1:
    media = soma / cont
    print('=-' * 15)
    print('Você inseriu {} números...\nA média entre eles foi: {}'.format(cont, media))
    print('O MAIOR valor foi: {}\nO MENOR valor foi: {}'.format(maior, menor))
else:
    print('Você só inseriu um valor ({})...'.format(n1))
