def notas(*num_f, situ_f=False):
    """
    Cadastro de notas_f
    :param num_f: Insira quantas notas_f precisar.
    :param situ_f: (opcional) mostrar situação da turma.
    :return: Função não retorna resultados.
    """
    notas_f = {'quantidade de notas': len(num_f), 'maior': max(num_f), 'menor': min(num_f),
               'media': sum(num_f) / len(num_f)}
    if situ_f:
        if notas_f['media'] < 5:
            notas_f['situ'] = 'REPROVADO!'
        elif notas_f['media'] < 7:
            notas_f['situ'] = 'RECUPERAÇÃO'
        else:
            notas_f['situ'] = 'APROVADO'
    return notas_f


turma = notas(7.7, 7.1, 6.4, 10, 8, situ_f=True)
print(turma)
