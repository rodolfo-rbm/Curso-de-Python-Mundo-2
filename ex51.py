'''desenvolva um programa que leia o
primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos
dessa progressão.'''

termo = int(input('Digite o 1º termo da nossa PA: '))
r = int(input('Agora digite a razão da nossa PA: '))
for c in range(termo, termo+10):
    print(termo, end=' >> ')
    termo += r
