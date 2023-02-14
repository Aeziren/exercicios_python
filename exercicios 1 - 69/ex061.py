pm = int(input('Primeiro termo da PA: '))
rz = int(input('Razão da PA: '))
print('[', end='')
meta = pm + (rz * 9)
while pm != meta:
    print('{}, '.format(pm), end='')
    pm = pm + rz
print('{}...]'.format(pm))
