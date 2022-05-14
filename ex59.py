'''Crie um programa que leia dois valores e mostre
um menu na tela:
[1] - somar
[2] - multiplicar
[3] - maior
[4] - novos números
[5] - sair do programa

- seu programa deverá realizar a operação solicitada em cada caso '''
from time import sleep
opcao = 0

while opcao !=5:

    opcao = int(input('Menu:'
                      '\n[1] - soma'
                      '\n[2] - multiplicar'
                      '\n[3] - maior'
                      '\n[4] - novos números'
                      '\n[5] - sair do programa'
                      '\n'
                      '\nDigite a opção desejada: '))
    if opcao == 1:
        print('Opção escolhida foi de soma.')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        sleep(0.5)
        print('Processando...')
        sleep(1)
        print('A soma de {} + {} = {}'.format(num1, num2, num1 + num2))
    elif opcao == 2:
        print('Opção escolhida foi de multiplicação.')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        sleep(0.5)
        print('Processando...')
        print('A multiplicação de {} x {} = {}'.format(num1, num2, num1 * num2))
    elif opcao == 3:
        print('Opção escolhida foi de mostrar o maior.')
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))
        if num1 > num2:
            sleep(0.5)
            print('Processando...')
            sleep(1)
            print('o número {} é maior que o número {}.'.format(num1, num2))
        else:
            sleep(0.5)
            print('Processando...')
            sleep(1)
            print('o número {} é maior que o número {}.'.format(num2, num1))
    elif opcao == 4:
        print('Opção escolhida foi a de digitar novos números.')

print('Opção escolhida foi a de encerrar o programa')
sleep(0.5)
print('Até uma próxima!!!')
