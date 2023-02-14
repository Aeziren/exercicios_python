import math
ang = float(input('Insira o ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('=' * 4, 'ÂNGULO DE {}:'.format(ang), '=' * 4, '\n')
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f}\n'.format(sen, cos, tan))
print('=' * 24)



