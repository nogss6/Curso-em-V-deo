def triangulo(r1, r2, r3):
    if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
        print('Os segmentos ==PODEM FORMAR== um triângulo')


r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 == r2 and r2 == r3 and r3 == r1:
    triangulo(r1, r2, r3)
    print('==TRIÂNGULO EQUILÁTERO==')
elif r1 == r2 or r2 == r3 or r3 == r1:
    triangulo(r1, r2, r3)
    print('==TRIÂNGULO ISÓCELES==')
else:
    triangulo(r1, r2, r3)
    print('==TRIÂNGULO ESCALENO==')
