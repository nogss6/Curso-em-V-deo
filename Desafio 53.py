f = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
i = (f[::-1])
if (f) == i:
    print('=PALÍNDROMO=')
else:
    print('=NÃO É PALÍNDROMO=')