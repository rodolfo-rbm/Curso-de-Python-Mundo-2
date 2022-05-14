'''Crie um programa que leia uma frase qualquer
e diga se ela é um palindromo, desconsiderando
os espaços'''

frase = str(input('Digite uma frase qualquer: ')).strip().lower()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
'''inverso == junto[::-1] / outra forma de fazer ai não precisa do for'''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('temos um palindromo.')
else:
    print('A frase não é um palindromo.')