num = int(input('Insira o número inteiro a ser convertido: '))
print('=' * 4, 'CONVERTER {} PARA: '.format(num), '=' * 4)
op = int(input('1 - BINÁRIO\n2 - OCTAL\n3 - HEXADECIMAL\nOpção: '))
if op == 1:
    num = format(num, 'b')
    print(num)
elif op == 2:
    num = format(num, 'o')
    print(num)
elif op == 3:
    num = format(num, 'x')
    print(num)
else:
    print('Opção Inválida!')
