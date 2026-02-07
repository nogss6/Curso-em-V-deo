def imc(p, a):
    return p/a


peso = float(input('Peso: '))
altura = float(input('Altura: '))
if imc(peso, altura) < 18.5:
    print('==ABAIXO DO PESO==')
elif imc(peso, altura) < 25:
    print('==PESO IDEAL==')
elif imc(peso, altura) < 30:
    print('==SOBREPESO==')
elif imc(peso, altura) < 40:
    print('==OBESIDADE==')
else:
    print('==OBESIDADE MÓRBIDA==')
