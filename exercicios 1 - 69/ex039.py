from datetime import date
ano = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = ano - nasc
if idade > 18:
    print('Seu ano de alistamento foi há {} ano(s)!'.format(idade - 18))
elif idade < 18:
    print('Seu ano de alistamento será daqui {} ano(s). Em {}!'.format(18 - idade, (18 - idade) + ano))
else:
    print('É o seu ano de alistamento!')



