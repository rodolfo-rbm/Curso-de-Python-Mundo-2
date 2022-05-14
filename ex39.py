'''Faça um programa que leia o ano de um jovem
e informe de acordo com sua idade:
- se ele ainda vai se alistar ao exercito
- se é hora de se alistar
- se já passou do tempo de alistamento
o programa também deverá mostrar quanto
tempo já passou do prazo'''
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano

if idade < 0:
    print('Opção inválida. Digite uma opção válida.')
elif idade < 18:
    print('Calma guerreiro, ainda não é hora de se alistar. Você tem apenas {} anos'.format(idade))
elif idade == 18:
    print('Parabéns guerreiro!!! Chegou a hora de se alistar. VocÊ tem {} anos'.format(idade))
else:
    print('O prazo para se alistar já foi. Infelizmente não é mais possível fazer o alistamento. Você tem {} anos'.format(idade))
