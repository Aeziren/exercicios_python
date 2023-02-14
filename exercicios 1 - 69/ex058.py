from random import randint
maq = randint(0, 10)
tent = 0
jog = int(input('Pensei em número inteiro, tente acertar qual é: '))
while jog != maq:
    if jog > maq:
        jog = int(input('MENOS... Tente de novo: '))
        tent += 1
    elif jog < maq:
        jog = int(input('MAIS... Tente de novo: '))
        tent += 1
if tent == 0:
    print('UAU! Você acertou de primeira! Era o {} mesmo...'.format(jog))
else:
    print('Acertou depois de {} tentativa(s), era o {} mesmo.'.format(tent, jog))
