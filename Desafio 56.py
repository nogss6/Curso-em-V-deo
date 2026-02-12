somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totf20 = 0
for c in range(1, 5):
    print(f'---- {c}° PESSOA ----')
    nome = str(input('Nome: ')).replace(' ', '')
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).replace(' ', '').upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maoridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totf20 += 1
mediaidade = somaidade / 4
print(f'A MÉDIA DE IDADE É == {mediaidade} ANOS')
print(f'O HOMEM MAIS VELHO TEM {maioridadehomem} ANOS E SE CHAMA {nomevelho}')
print(f'TEM {totf20} MULHERES COM MENOS DE 20 ANOS')
