def menu():
    cabeçalho('MENU PRINCIPAL')
    print('\033[36m1-\033[m Ver pessoas cadastradas\n'
          '\033[36m2-\033[m Cadastrar nova pessoa.\n'
          '\033[36m3-\033[m Sair do sistema.')
    print('=' * 30)
    while True:
        op = str(input('\033[36m Opção: \033[m'))
        if op in '123':
            return op
        else:
            print('\033[31mOpção inválida!\033[m')


def mostrar(nome_f):
    try:
        txt = open(f'{nome_f}.txt', 'r')
    except FileNotFoundError:
        print('\033[31mArquivo não encontrado!\033[m')
    else:
        cabeçalho('EXIBINDO DADOS')
        print(f'{" Nome":<24}{"Idade"}')
        print('-' * 30)
        for l in txt:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<24}{dado[1]:^5}')

def cadastrar(txt_f, nome_f='<desconhecido>', idade=0):
    try:
        txt = open(f'{txt_f}.txt', 'a+')
    except FileNotFoundError:
        print(f'\033[31mArquivo {txt_f} não encontrado!\033[m')
    else:
        print('=' * 30)
        txt.write(nome_f)
        txt.write(';')
        txt.write(str(idade))
        txt.write('\n')
        print(f'{nome_f} foi adicionado com sucesso!')
        txt.close()



def abrir_arquivo(nome_f):
    try:
        txt = open(f'{nome_f}.txt', 'x')
    except FileExistsError:
        print('Arquivo aberto!')
    else:
        print(f'{nome_f} foi criado com sucesso!'.capitalize())
        txt.close()


def leia_int(txt_f):
    while True:
        try:
            num = int(input(txt_f))
            break
        except ValueError:
            print('\033[31mValor Inválido.\033[m')
    return num


def cabeçalho(txt_f):
    print('=' * 30)
    print(f'\033[32m{txt_f:^30}\033[m')
    print('=' * 30)
