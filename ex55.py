'''faça um programa que leia o peso de 5 pessoas
e no final mostre qual doi o maior e o menor peso.'''
maiorpeso = 0
menorpeso = 0
for i in range(1, 6):
    peso = int(input('Peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maiorpeso = i
        menorpeso = i
    else:
        if peso > maiorpeso:
            maiorpeso = peso
        if peso < menorpeso:
            menorpeso = peso


print('O maior peso digitado foi de {} Kg'.format(maiorpeso))
print('O menor peso digitado foi de {} Kg'.format(menorpeso))
