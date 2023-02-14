cidade = str(input('Insira o arq da cidade: ')).strip()
cidade = cidade.title()
print('Analisando: {}...\nComeça com Santo? {}'.format(cidade, cidade.startswith('Santo')))
