'''elabore um programa que calcule o valor a ser
pago por um produto, considerando o seu
preço normal e condição de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros'''
from time import sleep
prod = float(input('Digite o valor do produto adquirido: R$ '))
print('-'*65)
num = int(input('Escolha uma das formas de pagamanto abaixo: \n'
                '1 - à vista no dinheiro / cheque: 10 % desconto.\n'
                '2 - Cartão de débito: 5 % desconto.\n'
                '3 - em até 2x no cartão: preço normal.\n'
                '4 - 3x ou mais no cartão: 20% de juros.\n'
                'Digite o número que corresponde a forma de pagamento desejada: '))
print('-'*65)
print('Processando...')
print('-'*65)
sleep(2)
if num == 1:
    print('Forma de pagamento escolhida foi à vista/cheque.\n'
          'Você terá um desconto de 10%.')
    print('O valor do produto já com desconto é de R$ {:.2f}'.format(prod*0.9))
elif num == 2:
    print('Forma de pagamento escolhida foi Cartão de débito.\n'
          'Você terá um desconto de 5%.')
    print('O valor do produto já com desconto é de R$ {:.2f}'.format(prod*0.95))
elif num == 3:
    print('Forma de pagamento escolhida foi em até 2x no cartão.\n'
          'Você pagará o preço normal do produto que é de R$ {:.2f}'.format(prod))
elif num == 4:
    print('Forma de pagamento escolhida foi 3x ou mais no cartão.\n'
          'Será cobrado 20% de juros em cima do valor do produto.')
    print('O valor do produto com o juros é de R$ {:.2f}'.format(prod*1.2))
else:
    print('Opção inválida. Tenta novamente!!!')

print('-'*65)
