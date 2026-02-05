frase = input('Digite uma frase: ').upper()
print(f'Aparece: {frase.count('A')} vezes')  # acento não conta como "A" normal
print('Primeira posição: ', frase.find('A'))
print('Ultima posição: ', frase.rfind('A'))
