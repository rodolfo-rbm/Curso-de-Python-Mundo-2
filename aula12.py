nome = str(input('Digite seu nome: ')).upper()
if nome == 'Rodolfo'.upper():
    print('Que nome bonito')
elif nome == 'maria'.upper() or nome == 'pedro'.upper() or nome == 'paulo'.upper():
    print('Seu nome é bem popular')
elif nome in 'Ana Julia Claudia Juliana'.upper():
    print('Belo nome feminino')
else:
    print('Seu nome é normal')
print('Tenha um bom dia {}'.format(nome))

