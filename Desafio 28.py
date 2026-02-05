import random
numeros = int(random.choice(range(6)))
escolha = int(input('Escolha um número de 0 até 5: '))
if escolha == numeros:
    print('VOCÊ ACERTOU!')
else:
    print(f'VOCÊ ERROU!, O NÚMERO CERTO ERA {numeros}')
print('==FIM DE JOGO==')
