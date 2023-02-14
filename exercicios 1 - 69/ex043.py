alt = float(input('Altura: '))
peso = float(input('Peso (KG): '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print('ABAIXO DO PESO! IMC: {:.1f}'.format(imc))
elif imc < 25:
    print('PESO IDEAL! IMC: {:.1f}'.format(imc))
elif imc < 30:
    print('SOBREPESO! IMC: {:.1f}'.format(imc))
elif imc < 40:
    print('OBESIDADE! IMC: {:.1f}'.format(imc))
else:
    print('OBESIDADE MÓRBIDA! IMC: {:.1f}'.format(imc))
