from datetime import date
dados = dict()
dados['arq'] = str(input('Nome: '))
dados['idade'] = date.today().year - int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('CTPS: '))
if dados['ctps'] == 0:
    print('=' * 30)
    print(f'Usuário tem {dados["idade"]} anos e não pode trabalhar. CTPS não emitida.')
else:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['contratação'] + 35) - (date.today().year - dados['idade'])
    print('=' * 30)
    for k, v in dados.items():
        print(f'{k}: {v}'.title())
