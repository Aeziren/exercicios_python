nome = str(input('Nome: ')).strip().title()
pm = nome[:nome.find(' ')]
um = nome[nome.rfind(' '):]
print('Este arq formatado é: {}{}'.format(pm, um))


