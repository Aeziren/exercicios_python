total = prod1000 = mais_barato = valor_mais_barato= qtd_prod = 0
while True:
    nome = str(input('Nome do Produto: ')).title().strip()
    preco = float(input('Preço €: '))
    if total == 0:
            valor_mais_barato = preco
            mais_barato = nome
    total += preco
    qtd_prod += 1
    if preco < valor_mais_barato:
        mais_barato = nome
        valor_mais_barato = preco
    if preco >= 1000:
        prod1000 += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar [S/N]? ')).strip().upper()
    if op == 'N':
        break
print('=' * 35, '\nMOSTRANDO RESULTADOS: ')
print(f'Você comprou {qtd_prod} produtos. Valor total da compra €: {total:.2f}')
print(f'Quantidade de produtos mais caros que € 1.000,00: {prod1000}')
print(f'Produto mais barato: {mais_barato}')
