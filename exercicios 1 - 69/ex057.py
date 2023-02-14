op = str(0)
while op not in 'MF':
    op = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if op not in 'MF':
        print('Tente novamente...')
if op == 'F':
    print('Você selecionou "Feminino", obrigado!')
else:
    print('Você selecionou "Masculino", obrigado!')
