'''desenvolva um programa que leia o nome, idade e
sexo de 4 pessoas e no final mostre:
- a média de idade do grupo
- qual o nome do homem mais velho
- quantas mulheres tem menos de 20 anos'''

soma = 0
homem = 0
mulher = 0
maisvelho = 0
nomemaisvelho = ''

for c in range(0, 4):
    nome = str(input('\nDigite seu primeiro nome: ')).lower()
    idade = int(input('\nDigite sua idade: '))
    sexo = str(input('\nDigite seu sexo (M para Masculino ou F para Feminino): ')).lower()

    soma += idade

    if sexo == 'f' and idade <= 20:
        mulher +=1

    elif sexo == 'm' and idade > maisvelho:
        maisvelho += idade
        nomemaisvelho = nome


print('A média de idade do grupo é de {:.0f} anos.'.format(soma/4))
print('{} mulheres tem menos de 20 anos.'.format(mulher))
print('O nome do homem mais velho é {}'.format(nomemaisvelho))

