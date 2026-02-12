maior = 0
menor = 0
for c in range(1, 6):
    p = float(input(f'Peso da {c}° pessoa: '))
    if c == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print(f'O MAIOR PESO É == {maior}')
print(f'O MENOR PESO É == {menor}')
