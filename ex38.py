'''Escreva um programa que leia dois números inteiros
e compare-os, mostrando na tela uma mensagem:
- o primeiro valor é maior
- o segundo valor é maior
- não existe valor maior, os dois são iguais'''

n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite outro número inteiro:'))

if n1 > n2:
    print('O primeiro valor é maior!!! {} é maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor é maior!!! {} é maior que {}'.format(n2, n1))
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais!!!')
