from datetime import date
ano = date.today().year
nasc = int(input('Ano de Nascimento do Atleta: '))
idade = ano - nasc
print('O atleta tem {} anos. Pertence à categoria: '.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
