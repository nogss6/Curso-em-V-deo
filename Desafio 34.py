salario = float(input('Salário: R$'))
if salario > 1250:
    novo_salario = ((salario/10)+salario)
    print(f'Novo Salário: R${novo_salario}\nAumento de {salario/10}')
else:
    novo_salario = {(salario*15/100)+salario}
    print(f'Novo Salário: R${novo_salario}\nAumento de {salario*15/100}')
