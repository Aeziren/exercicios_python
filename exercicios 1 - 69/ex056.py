media = 0
idade_hom = 0
nome_hom = str('Nenhum homem inserido...')
qtt_mulh = 0
for pessoa in range(1, 5):
    nome = str(input('Nome da {}ª dados: '.format(pessoa))).title().strip()
    idade = int(input('Idade da {} dados: '.format(pessoa)))
    print('Sexo da {} dados...'.format(pessoa))
    sexo = str(input('[ M ] para Masculino\n[ F ] para Feminino\nOpção: '.format(pessoa))).strip().upper()
    media = media + idade
    if sexo == 'M':
        if idade > idade_hom:
            idade_hom = idade
            nome_hom = nome
    else:
        if idade < 20:
            qtt_mulh = qtt_mulh + 1
print('ANALISANDO OS DADOS INSERIDOS...')
print('Idade média das pessoas: {:.1f}'.format(media / 4))
print('O homem mais velho é: {} ({} Anos)'.format(nome_hom, idade_hom))
print('Quantidade de mulheres com menos de 20 anos: {}'.format(qtt_mulh))







