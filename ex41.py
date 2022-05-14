'''A confedereção nacional de natação precisa
de um programa que leia o ano de nascimento de
um atleta e mostre sua categoria, de acordo
com sua idade
- até 9 anos: Mirim
- até 14 anos: infantil
- até 19 anos: junior
- até 20 anos: senior
- acima de 20 anos: master'''
from datetime import date
ano = int(input('Digite seu ano de nascimento para saber qual sua categoria: '))
idade = date.today().year - ano

if ano > date.today().year:
    print('Opção invalída.')
elif idade <= 9:
    print('Sua idade é de {} anos, portanto sua categoria é Mirim.'.format(idade))
elif idade > 9 and idade <= 14:
    print('Sua idade é de {} anos, portanto sua categoria é Infantil.'.format(idade))
elif idade > 14 and idade <= 19:
    print('Sua idade é de {} anos, portanto sua categoria é Junior.'.format(idade))
elif idade == 20:
    print('Sua idade é de {} anos, portanto sua categoria é Senior.'.format(idade))
elif idade > 20:
    print('Sua idade é de {} anos, portanto sua categoria é Master.'.format(idade))
else:
    print('Opção inválida.')
