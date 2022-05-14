'''faça um programa que mostre na tela
uma contagem regressiva para o estouro
de fogos de artificio, indo de 10 até
0, com uma pausa de 1 sec entre eles'''

from time import sleep
from emoji import demojize

print('Iremos iniciar a contagem regressiva para os fogos!!!')
for c in range(10, -1, -1):
    sleep(1)
    print(c)

sleep(1)
print('\n\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5\U0001F4A5')


