print('=========DESAFIO22=========')
nome = str(input('Digite Seu Nome Completo: ')).strip()
print('Analisando seu nome........')
print('Seu nome em maiusculas é {}: '.format(nome.upper()))
print('Seu nome em  minusculas é {}: '.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(separa[0], nome.find(' ')))
