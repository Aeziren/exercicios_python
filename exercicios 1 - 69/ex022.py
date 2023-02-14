nome = str(input('Nome: '))
print('Seu arq em maiúsculas é: {}'.format(nome.upper()))
print('Seu arq em minúsculas é: {}'.format(nome.lower()))
print('Seu arq tem {} letras.'.format(len(nome) - nome.count(' ')))
nome = nome.split()
print('O primeiro arq tem {} letras.'.format(len(nome[0])))




