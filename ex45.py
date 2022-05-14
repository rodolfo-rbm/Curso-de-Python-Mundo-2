'''crie um programa que faça o computador
 jogar jokenpô com você.'''
from time import sleep
import random
print('Vamos jogar Jokenpô! Estou animado para te vencer...')
print('-'*52)
escolha = str(input('Vamos jogar... Qual você escolhe?\n'
              'pedra, papel ou tesoura? ')).upper()
lista = ['pedra'.upper(), 'papel'.upper(), 'tesoura'.upper()]
comp = random.choice(lista)

if escolha != 'tesoura'.upper() and escolha != 'papel'.upper() and escolha != 'pedra'.upper():
    print('Opção inválida. Escolha entre pedra, papel ou tesoura.')
elif escolha == 'tesoura'.upper() and comp == 'papel'.upper():
    print('JO')
    sleep(1)
    print(('KEN'))
    sleep(1)
    print('PO!!!')
    print('Parabéns... Você ganhou do computador.')
    print('{} ganha de {}'.format(escolha, comp).lower())
elif escolha == 'papel'.upper() and comp == 'pedra'.upper():
    print('JO')
    sleep(1)
    print(('KEN'))
    sleep(1)
    print('PO!!!')
    print('Parabéns... Você ganhou do computador.')
    print('{} ganha da {}'.format(escolha, comp).lower())
elif escolha == 'pedra'.upper() and comp == 'tesoura'.upper():
    print('JO')
    sleep(1)
    print(('KEN'))
    sleep(1)
    print('PO!!!')
    print('Parabéns... Você ganhou do computador.')
    print('{} ganha da {}'.format(escolha, comp).lower())
elif escolha == comp:
    print('JO')
    sleep(1)
    print(('KEN'))
    sleep(1)
    print('PO!!!')
    print('Ninguém venceu. Os dois escolheram a mesma opção.')
    print('{} com {} da empate.'.format(comp, escolha).lower())
else:
    print('JO')
    sleep(1)
    print(('KEN'))
    sleep(1)
    print('PO!!!')
    print('Não foi dessa vez. O computador te venceu.')
    print('{} ganha de {}'.format(comp, escolha).lower())

