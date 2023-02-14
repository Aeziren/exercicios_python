lista = ('comida', 'amigo', 'legal', 'vitoria', 'conquista', 'familia', 'feliz', 'jogo',
         'aniversario', 'ferramentas', 'python', 'sucesso', 'orgulho', 'beleza', 'academia',
         'amor', 'pensamento', 'livro', 'superficie', 'final', 'paz')
for palavra in lista:
    print(f'A palavra {palavra.upper()} tem as vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
    print('\n')