import random
opçoes = ['Pedra', 'Papel', 'Tesoura']

print('Escolha uma opção: ')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')
jogador = int(input('Sua escolha: '))
maquina = random.randint(0, 2)
print(f'Você escolheu {[jogador]}')
print(f'A máquina escolheu {[maquina]}')

if jogador == maquina:
    print('==EMPATE==')
elif jogador == 0 and maquina == 2:
    print('==VOCÊ GANHOU==')
elif jogador == 1 and maquina == 0:
    print('==VOCÊ GANHOU==')
elif jogador == 2 and maquina == 1:
    print('==VOCÊ GANHOU==')
else:
    print('==VOCÊ PERDEU==')
