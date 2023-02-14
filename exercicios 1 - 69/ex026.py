frase = str(input('Digite uma frase qualquer: ')).strip().lower()
print('A letra -A- aparece nesse texto {} vezes.'.format(frase.count('a')))
print('A primeira vez que ela aparece é na posição {}'.format(frase.find('a') + 1))
print('E aparece pela última vez na posição {}.'.format(frase.rfind('a') + 1))

