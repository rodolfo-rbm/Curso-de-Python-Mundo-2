'''refaça o desafio 51, lendo o primeiro termo e a razao
de uma PA, mostrando os 10 primeiros termos da progressao
usando a estrutura WHILE'''

termo = int(input('Digite o 1º termo da nossa PA: '))
r = int(input('Agora digite a razão da nossa PA: '))

cont = 0
while cont <= 10:
    print(termo, end=' >> ')
    termo += r
    cont += 1

