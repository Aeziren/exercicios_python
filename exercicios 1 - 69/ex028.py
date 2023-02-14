from random import randint
from time import sleep
num = randint(0, 5)
print('=' * 5, 'Jogo da Adivinhação', '=' * 5)
n1 = int(input('Tente acertar o número que a máquina pensou: '))
print('Processando...')
sleep(2)
if n1 == num:
    print('Parabéns, você acertou!! Era {} mesmo'.format(n1))
else:
    print('Tente de novo! Era {}.'.format(num))
print('=' * 3, 'Obrigado por jogar!', '=' * 3)

