'''desenvolva um exercicio que leia seis
números inteiros e mostre a soma apenas
daqueles que forem pares. Se o valor
digitado for ímpar desconsidere-o'''

s = 0
a = 0
b = 6
for c in range(a, b):
    num = int(input('Digite um número inteiro: '))
    if num % 2 == 0:
        s += num

print('A soma dos números pares é {}'.format(s))
