'''refaça o desafio 35, acrescentando o recurso
 de mostrar o tipo de triângulo que será formado
 - equilatero: 3 lados iguais
 - isóceles: dois lados iguais
 - escaleno: todos lados diferentes'''

reta1 = float(input('Digite o valor da reta 1: '))
reta2 = float(input('Digite o valor da reta 2: '))
reta3 = float(input('Digite o valor da reta 3: '))

if (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta1 + reta3) > reta2:
    print('É possível formar um triângulo.')

else:
    print('Não é possível formar um triângulo.')

if reta2 == reta1 == reta3:
    print('Esse triângulo é equilatero, ou seja, todos os lados são iguais.')
elif (reta1 == reta2 and reta1 != reta3) or (reta2 == reta3 and reta2 != reta1) or (reta3 == reta1 and reta3 !=reta2):
    print('Esse triângulo é isóceles, ou seja, possui dois lados iguais.')
elif reta2 != reta1 != reta3:
    print('Esse triângulo é escaleno, ou seja, todos os lados são diferentes.')
