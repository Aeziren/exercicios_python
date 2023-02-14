print('=== Detector de Palíndromo ===')
frase = str(input('Digite uma frase: ')).upper().replace(' ', '')
rev = frase[::-1]
print(rev)
if frase == rev:
    print('Essa frase é um palíndromo!')
else:
    print('Não é um palíndromo!')