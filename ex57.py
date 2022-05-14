'''faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores M ou F. Caso esteja errado,
peça a digitação novamente até ter um valor correto.'''
sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite qual o seu sexo: M para masculino ou F para feminino... ').upper())
    if sexo != 'F' and sexo != 'M':
         print('Opção Inválida...Tente novamente.')
    else:
        if sexo == 'F':
            print('Opção escolhida foi sexo feminino.')
        else:
            print('Opçao escolhida foi sexo masculino.')