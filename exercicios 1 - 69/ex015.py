dias = int(input('Dias alugados: '))
km = float(input('Kms percorridos: '))
r = (dias * 60) + (km * 0.15)
print('O valor a pagar referente a {} dias locados e {:.1f} Km percorridos é de {:.2f}€'.format(dias, km, r))

