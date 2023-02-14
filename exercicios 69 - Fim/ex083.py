abertos = fechados = 0
expressao = str(input('Digite a expressão: '))
hier_correto = True
for char in expressao:
    if char in '(':
        abertos += 1
    if char in ')':
        fechados += 1
    if fechados > abertos:
        print('Expressão Incorreta. Hierarquia não respeitada!')
        hier_correto = False
        break
if hier_correto:
    if abertos != fechados:
        print('Expressão Incorreta. Parênteses não fechados!')
    else:
        print('Expressão Correta!')
