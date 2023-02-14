salario = float(input('Digite o salário: '))
if salario > 1250:
    salario = (salario * 10 / 100) + salario
    print('Receberá um aumento de 10% e o novo salário será: €{:.2f}'.format(salario))
else:
    salario = (salario * 15 / 100) + salario
    print('Receberá um aumento de 15% e o novo salário será: €{:.2f}'.format(salario))
