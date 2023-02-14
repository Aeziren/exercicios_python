from time import sleep


def maior(*num):
    maior_f = 0
    print('Analisando o valor...')
    for pos, n in enumerate(num):
        print(f'{n}...', end='')
        sleep(0.4)
        if pos == 0:
            maior_f = n
        else:
            if n > maior_f:
                maior_f = n
    print('\n', '=' * 30, f'\nO maior valor é {maior_f}')


maior(1, 3, 5, 10, 2, 8, 9)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()