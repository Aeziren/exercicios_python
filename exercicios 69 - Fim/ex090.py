nome = str(input('Nome: '))
dados = {'arq': nome, 'media': float(input(f'Média de {nome}: '))}
if dados['media'] >= 7:
    dados['situação'] = 'aprovado'
elif dados['media'] > 5:
    dados['situação'] = 'recuperação'
else:
    dados['situação'] = 'reprovado'
print(f'{"Exibindo dados:":=^30}')
print(f'Nome do Aluno: {dados["arq"]}\nMédia: {dados["media"]}\nSituação: {dados["situação"]}')


