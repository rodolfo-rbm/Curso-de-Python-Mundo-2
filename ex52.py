'''faça um programa que leia um número
inteiro e diga se ele é ou não um número primo.'''

num = int(input('Digite um número inteiro: '))

if num < 2:
    print('Não é um número primo.')
elif num == 2:
    print(('2 é o único par que é primo.'))
else:
    for c in range(2, num):
        if num % c == 0:
            print('{} não é um número primo'.format(num))
    else:
        print('{} é número primo.'.format(num))