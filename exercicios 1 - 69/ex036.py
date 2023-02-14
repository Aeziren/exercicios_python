vcasa = float(input('Valor do Imóvel: '))
anos = int(input('Em quantos anos pretende pagar? ')) * 12
parc = vcasa / anos
vrenda = float(input('Sua renda mensal: ')) * 0.3
if vrenda >= parc:
    print('Empréstimo Aprovado!')
    print('Você pagará parcelas de €{:.2f} e 30% do seu salário é: €{}'.format(parc, vrenda))
else:
    print('Empréstimo Negado!')
    print('Você deveria conseguir pagar parcelas de €{:.2f} e 30% da sua renda mensal é: €{:.2f}'.format(parc, vrenda))






