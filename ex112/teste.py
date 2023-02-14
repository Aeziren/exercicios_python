from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado


num = dado.leiadinheiro('Valor: €')
acrescimo = int(input('Acrescimo: '))
desconto = int(input('Desconto: '))
op = str(input('Formatar em unidades monetárias? [S/N] ')).strip().upper()[0]
if op in 'S':
    formt = True
else:
    formt = False
moeda.resumo(num, acrescimo, desconto, formt)
