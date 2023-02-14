from random import choice
from time import sleep
player = str(input('PEDRA, PAPEL OU TESOURA? ')).strip().upper()
print('JO')
sleep(0.6)
print('KEN')
sleep(1.2)
print('PÔ!!!')
lista = ['PEDRA', 'PAPEL', 'TESOURA']
maq = choice(lista)
print('Escolha da Máquina: {}'.format(maq))
if player == 'PEDRA' and maq == 'TESOURA' or player == 'PAPEL' and maq == 'PEDRA' or player == 'TESOURA' and maq == 'PAPEL':
    print('VOCÊ VENCEU!!!')
elif player == maq:
    print('EMPATE! Vamos de novo!')
else:
    print('Você Perdeu! Tente novamente.')
