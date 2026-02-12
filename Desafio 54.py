from datetime import date
at = date.today().year
maioridade = 0
menoridade = 0
for c in range(1, 8):
    n = int(input(f'Ano de nascimento da {c}° pessoa: '))
    idade = at - n
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print(f'MAIORES DE IDADE == {maioridade}')
print(f'MENORES DE IDADE == {menoridade}')
