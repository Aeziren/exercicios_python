print('LOJA ABUSIVA')
valor = float(input('Valor do Produto: € '))
pag = int(input('''Metodo de Pagamento:
1 - Cheque ou Dinheiro à Vista.
2 - Cartão.
Opção: '''))
if pag == 1:
    print('O valor a ser pago é: € {:.2f}'.format(valor - (valor * 10 / 100)))
elif pag == 2:
    parc = int(input('Parcelas: '))
    if parc == 1:
        valorf = valor - (valor * 5 / 100)
        print('Você pagará ({}) parcela de € {:.2f}!'.format(parc, valorf))
    elif parc == 2:
        valorp = valor / parc
        print('Você pagará ({}) parcelas de € {:.2f}: TOTAL:€ {:.2f}'.format(parc, valorp, valor))
    elif 12 >= parc >= 3:
        valorf = valor + (valor * 20 / 100)
        valorp = valorf / parc
        print('Você pagará ({}) parcelas de € {:.2f}: TOTAL:€ {:.2f}'.format(parc, valorp, valorf))
    else:
        print('Opção Inválida!')
else:
    print('Opção Inválida!')
