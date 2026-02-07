n = int(input('Digite um número inteiro: '))
print('1-BINÁRIO')
print('2-OCTAL')
print('3-HEXADECIMAL')
bs = int(input('Sua Opção: '))
if bs == 1:
    print(bin(n)[2:])
elif bs == 2:
    print(oct(n)[2:])
elif bs == 3:
    print(hex(n)[2:].upper())
else:
    print('==OPÇÃO INVÁLIDA==')
