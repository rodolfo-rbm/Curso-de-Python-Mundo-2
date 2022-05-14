'''refaça o desafio 9, mostrando a tabuada
de um número que o usuário escolher, só que
agora utilizando o laço FOR'''
from time import sleep
num = int(input('Digite um número para a tabuada: '))
print('-'*15)
for c in range(1,11):
    sleep(0.5)
    print('{} X {} = {}'.format(c, num, c * num))
print('-'*15)

