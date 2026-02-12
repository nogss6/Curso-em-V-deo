n = int(input('Digite um número: '))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        t += 1
if t == 2:
    print('=NÚMERO PRIMO=')
else:
    print('=NÃO É NÚMERO PRIMO=')
