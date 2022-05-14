'''Escreva um programa que leia um número
inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 - binário
2 - octal
3 - hexadecimal'''

num = int(input('Digite um número inteiro: '))

print('-'*35)
print(('Agora iremos converter esse número.'))
print('-'*35)
print('Escolha uma das opções abaixo:')
print('1 - Binário\n2 - octal\n3 - Hexadecimal')
print('-'*35)
opcao = int(input('Digite a opção escolhida: '))
print('-'*35)
if opcao == 1:
    bin = format(num,'b')
    print('A conversão em binário é: {}'.format(bin))
    print('-' * 35)
elif opcao == 2:
    octal = format(num,'o')
    print('A conversão em octal é: {}'.format(octal))
    print('-' * 35)
elif opcao == 3:
    hex = format(num,'X')
    print('A conversão em hexadecimal é: {}'.format(hex))
    print('-' * 35)
else:
    print('Opção inválida!!! Tente uma das opções acima.')
    print('-' * 35)

