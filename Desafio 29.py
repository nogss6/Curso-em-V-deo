velocidade = int(input('Velocidade do carro: '))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print(F'VOCÊ FOI MULTADO EM {multa}')
    print('DIRIJA COM RESPONSABILIDADE!')
else:
    print('BOA VIAGEM!')
