from datetime import date
nascimento = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual-nascimento
if idade < 18:
    falta = 18-idade
    print(f'Ainda faltam {falta} anos para se alistar')
elif idade == 18:
    print('Está na hora de se alistar')
else:
    passou = idade-18
    print(f'Já se passou {passou} anos do prazo')
