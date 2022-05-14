'''Escreva um programa para aprovar
um emprestimo bancario para a compra
de uma casa. O programa vai perguntar
o valor da casa, o salario do comprador
e em quantos anos ele vai pagar. Calcule
o valor da prestação mensal, sabendo que
 ela não pode exceder 30% do salário ou
 então o empréstimo será negado'''

casa = float(input('Qual o valor da casa que você deseja comprar? R$ '))
salario = float(input('Qual o teu salário atual? R$ '))
ano = int(input('Quantos anos deseja pagar o imóvel?'))
valor = casa / (ano*12)

if valor < (salario*0.3):
    print('O Valor da prestação é de R$ {:.2f}, e ficou abaixo de 30% do seu salário.'.format(valor))
    print('Parabéns!!! Você conseguiu o empréstimo.')
else:
    print('O valor da prestação é de R$ {:.2f}, e ficou acima de 30% do seu salário.'.format(valor))
    print('Infelizmente o empréstimo foi negado.')
