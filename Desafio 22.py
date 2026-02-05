nome = input('Digite um nome: ')
print(nome.upper())
print(nome.lower())
nse = len(nome.replace(' ', ''))  # strip só remove das extremidades
print(f'Letras sem espaço: {len(nse)}')
pm = nome.split()[0]  # divide o nome e pega a 1° parte
print(f'Letras no primeiro nome: {len(pm)}')
