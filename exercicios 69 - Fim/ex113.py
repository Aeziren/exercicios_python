def leia_int(txt_f):
    while True:
        try:
            num = int(input(txt_f))
        except ValueError:
            print('Por favor insira um valor válido!')
        except KeyboardInterrupt:
            print('\nUsuário cancelou operação.')
            return 0
        else:
            return num


def leia_real(txt_f):
    while True:
        try:
            num = str(input(txt_f)).replace(',', '.').strip()
            num = float(num)
        except ValueError:
            print('Por favor insira um valor válido!')
        except KeyboardInterrupt:
            print('\nUsuário cancelou operação.')
            return 0
        else:
            return num


n1 = leia_int('Valor Inteiro: ')
print(n1)
n2 = leia_real('Valor Real: ')
print(n2)
