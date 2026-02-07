preço = float(input('Valor do produto: '))

print('Formas de pagamento: ')
print('1 - À vista no dinheiro/cheque')
print('2 - À vista no cartão')
print('3 - Em até 2x no cartão')
print('4 - 3x ou mais no cartão')

opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    vcd = preço-(preço/10)
    print(f'Valor a ser pago: {vcd}')

elif opcao == 2:
    vcd = preço-(preço/20)
    print(f'Valor a ser pago: {vcd}')

elif opcao == 3:
    print(f'Valor a ser pago: {preço}')

elif opcao == 4:
    vcj = preço+(preço/5)
    print(f'Valor a ser pago: {vcj}')

else:
    print('==Opção inválida==')
