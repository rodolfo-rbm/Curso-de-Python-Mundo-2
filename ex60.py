'''Faça um programa que leia um número qualquer e mostre
o seu fatorial - EX: 5! = 5x4x3x2x1 = 120'''

num = int(input('Digite um número: '))
cont = num
f = 1
print('Calculando {}! = '.format(num), end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    f = f * cont
    cont -= 1
print('{}'.format(f))
