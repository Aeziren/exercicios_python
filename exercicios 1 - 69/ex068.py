from random import randint
vitorias = 0
result = 0
while True:
    op = ' '
    while op not in 'PI':
        op = str(input('Você quer PAR ou ÍMPAR [P/I]: ')).strip().upper()[0]
    jog = int(input('Insira um valor: '))
    maq = randint(0, 10)
    print(f'Computador jogou: {maq}\n', '=' * 35)
    total = maq + jog
    result = total % 2
    if op in 'P' and result == 0 or op in 'I' and result == 1:
        print(f'Total: {total}\nVOCÊ VENCEU! Vamos de Novo!\n')
        vitorias += 1
    else:
        break
print(f'Total: {total}\nVocê Perdeu!\nVitorias: {vitorias}\n')
