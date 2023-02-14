alt = float(input('Qual a altura da parede? '))
lrg = float(input('Qual a largura da parede? '))
res = alt * lrg
print('Essa parede tem {:.1f} m², para pintar essa parede você ira precisar de {:.1f} litros de tinta'.format(res, res / 2))
