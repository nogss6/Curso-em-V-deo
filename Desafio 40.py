n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
m = (n1+n2)/2
if m < 5.0:
    print('==REPROVADO==')
elif m >= 5.0 and m <= 6.9:
    print('==RECUPERAÇÃO==')
else:
    print('==APROVADO==')
