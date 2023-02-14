vel = float(input('Velocidade: '))
if vel > 80:
    multa = float((vel - 80) * 7)
    print('Você foi multado por excesso de velocidade!\nValor da Multa: €{:.2f}'.format(multa))
else:
    print('Parabéns! Dentro da velocidade permitida.')
