'''Melhore o jogo do desafio 28 onde o computador
vai pensar em um número de 0 a 10. Só que agora o
jogador vai tentar adivinhar até acertar, mostrando
no final quantos palpites foram necessários para vencer'''

import random
from time import sleep
cont = 0
num2 = 0
num = random.randint(0, 10)
while num2 != num:
    num2 = int(input('Digite um numero e veja se foi o mesmo escolhido pela maquina: '))
    cont += 1
print('Processando...')
sleep(2)
if num == num2:
    print('Parabéns, você venceu o computador')
print('Você precisou de {} tentativas para vencer o computador.'.format(cont))
