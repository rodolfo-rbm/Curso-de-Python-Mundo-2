'''faça um programa que calcule a soma entre
todos os números impares que são multiplos de
3 e que se encontram num intervalo de 1 até 500'''
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c

print(s)
