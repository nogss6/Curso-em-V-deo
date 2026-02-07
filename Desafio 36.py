casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = float(input('Quantos anos: '))
prestaçao = casa/(anos*12)
if prestaçao > (salario*30)/100:
    print('==EMPRÉSTIMO NEGADO==')
else:
    print('==EMPRÉSTIMO APROVADO==')
