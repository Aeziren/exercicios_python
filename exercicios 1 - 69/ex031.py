km = float(input('Distância da viagem: '))
if km >= 200:
    print('Você pagará €0,45 por km! Totalizando €{:.2f}'.format(km * 0.45))
else:
    print('Você pagará €0,50 por km! Totalizando €{:.2f}'.format(km * 0.50))

