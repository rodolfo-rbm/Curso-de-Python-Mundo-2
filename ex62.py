'''melhore o desafio 61, perguntando para o usuário
se ele quer mostrar mais alguns termos. O programa
encerra quando ele disser que quer mostrar 0 termos.'''

termo = int(input('Digite o 1º termo da nossa PA: '))
r = int(input('Agora digite a razão da nossa PA: '))

cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(termo, end=' >> ')
        termo += r
        cont += 1
    mais = int(input('\nQuantos termos você quer mostrar a mais? '))
