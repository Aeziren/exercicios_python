n1 = int(input('Número Inteiro: '))
verif = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        verif = verif + 1
if verif > 2 or verif == 1:
    print('Esse número pôde ser dividido por {} números! NÃO É PRIMO!'.format(verif))
elif verif == 2:
    print('Esse número é PRIMO!')
