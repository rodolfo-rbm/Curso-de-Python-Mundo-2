'''desenvolva uma lógica que leia o peso
e a altura de uma pessoa, calcule seu IMC
e omsetre seus status, de acordo com a tabela
- < 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 30 a 40:obesidade
- > 40: obesidade mórbida'''

from time import sleep

peso = float(input('Digite seu peso atual (Kg): '))
altura = float(input('Digite sua altura em metros: '))
print('-'*33)
print('Calculando...')
print('-'*33)
sleep(2)
imc = peso / (altura**2)
if imc < 18.5:
    print('Seu IMC é de {:.2f}\nVocê esta abaixo do peso ideal.'.format(imc))
    print('-' * 33)
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é de {:.2f}\nVocê está com o peso ideal.'.format(imc))
    print('-' * 33)
elif imc > 25 and imc < 30:
    print('Seu IMC é de {:.2f}\nVocê está com sobrepeso.'.format(imc))
    print('-' * 33)
elif imc > 30 and imc < 35:
    print('Seu IMC é de {:.2f}\nVocê esta com obesidade grau I.'.format(imc))
    print('-' * 33)
elif imc >= 35 and imc < 40:
    print('Seu IMC é de {:.2f}\nVocê esta com obesidade grau II.'.format(imc))
    print('-' * 33)
elif imc >= 40:
    print('Seu IMC é de {:.2f}\nVocê esta com obesidade grau III.'.format(imc))
    print('-' * 33)
else:
    print('Opção inválida!!!')