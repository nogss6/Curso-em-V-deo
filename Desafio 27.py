nome = input('Digite um nome: ').strip()
partes = nome.split()

print(f'Nome Completo: {nome}')
print(f'Primeiro Nome: {partes[0]}')
print(f'Último Nome: {partes[-1]}')  # O Python aceita índices negativos
