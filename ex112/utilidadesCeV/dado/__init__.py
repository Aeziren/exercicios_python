def leiadinheiro(txt):
    while True:
        num = str(input(txt).strip().replace(',', '.'))
        if num.isalpha():
            print('Inválido! Insira somente números.')
        elif not num:
            print('Digite algo.')
        else:
            num = float(num)
            break
    return num
