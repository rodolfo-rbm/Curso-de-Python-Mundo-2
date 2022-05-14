'''crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são
maiores'''

from datetime import date
menor = 0
maior = 0
atual = date.today().year
for i in range(0, 7):
    nasc = int(input('Digite seu ano de nascimento: '))
    if (atual - nasc) < 21:
      menor += 1
    else:
        maior +=1

print('{} pessoas são menores de idade'.format(menor))
print('{} pessoas são maiores de idade'.format(maior))
