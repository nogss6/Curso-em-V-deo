viagem = int(input('Distância da viagem em km: '))
if viagem <= 200:
    print(f'A viagem custou: R${viagem*0.50}')
else:
    print(f'A viagem custou: R${viagem*0.45}')
