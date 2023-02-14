n1 = float(input('Primeira notas: '))
n2 = float(input('Segunda notas: '))
media = (n1 + n2) / 2
if media < 5:
    print('Sua média é {:.1f}. Aluno está Reprovado!'.format(media))
elif 5 <= media < 7:
    print('Sua média é {:.1f}. Aluno está de Recuperação!'.format(media))
else:
    print('Sua média é {:.1f}. Aluno foi APROVADO!'.format(media))
