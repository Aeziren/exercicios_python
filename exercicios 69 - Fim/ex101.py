def eleitor(ano_f):
    from datetime import date
    idade = date.today().year - ano_f
    if idade >= 65:
        return f'Com {idade} anos. VOTO OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos. VOTO OBRIGATÓRIO'
    elif idade >= 16:
        return f'Com {idade} anos. VOTO OPCIONAL'
    else:
        return f'Com {idade} anos. VOTO NEGADO'


ano = int(input('Ano de nascimento: '))
print(eleitor(ano))
