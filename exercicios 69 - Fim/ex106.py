def manual(comando_f):
    print('\033[7;38m')
    help(comando_f)
    print('\033[m')


while True:
    print('\033[0;42m~' * 30, '\n Ajuda Interativa do Python!')
    print('~' * 30)
    comando = str(input('\033[mComando: ')).lower().strip()
    if comando in 'fim':
        print('\033[0;31mObrigado por usar a ajuda interativa!\033[m')
        break
    manual(comando)
