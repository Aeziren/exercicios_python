from EX115.funcoes import *
from time import sleep

arq = 'pessoas'
abrir_arquivo(arq)
while True:
    op = menu()
    if op in '1':
        mostrar(arq)
    elif op in '2':
        cabeçalho('CADASTRANDO')
        nome = str(input('Nome: '))
        idade = leia_int('Idade: ')
        cadastrar(arq, nome, idade)
    elif op in '3':
        break
    sleep(2)
print('=' * 30)
print('\033[32m<Desligando...>\033[m')
