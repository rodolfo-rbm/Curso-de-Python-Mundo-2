'''Crie um programa que leia duas notas
de um aluno e calcule a sua média, mostrando
uma mensagenm no final de acordo com a média atigida
- média abaixo de 5: Reprovado
- média entre 5 e 6.9: recuperação
- médias acima de 6.9: aprovado'''
from time import sleep
print('-'*60)
materia = input('Digite a matéria desejada para saber a média do 1º semestre: ')
nota1 = float(input('Digite sua nota em {} do primeiro bimestre: '.format(materia)))
nota2 = float(input('Digite sua nota em {} do segundo bimestre: '.format(materia)))
print('-'*60)
print('Calculando...')

media: float = (nota1 + nota2)/2
sleep(2)
if media < 5:
    print('Sua média foi de {:.2f} em {}.'.format(media, materia))
    print('Você foi reprovado. Você precisa estudar muito mais')
elif media >= 5 and media <= 6.9:
    print('Sua média foi de {:.2f} em {}.'.format(media, materia))
    print('Você ficou de recuperação. Estude um pouco mais.')
elif media >= 7:
    print('Sua média foi de {} em {}'.format(media, materia))
    print('Parabéns, você foi aprovado!!!')
