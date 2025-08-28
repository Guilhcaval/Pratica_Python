# 1º Questão
numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O seu número é par')
else:
    print('O seu número é ímpar')

# 2º Questão
number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))

if number1 > number2:
    print(f'{number1}')
elif number1 == number2:
    print('Os números são iguais')
else:
    print(f'{number2}')

# 3º Questão
letra = input('Digite uma letra: ')

if (letra in 'aeiou'):
    print('Vogal')
else:
    print('Consoante')

# 4º Questão
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/ 2

if media == 10:
    print('Aprovado com Distinção')
elif media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado')

# 5º Questão
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))

if num1 > num2 and num3:
    print(f'{num1}')
elif num2 > num3 and num1:
    print(f'{num2}')
elif num3 > num1 and num2:
    print(f'{num3}')

# 6º Questão
turno = input('Digite o turno no qual você estuda\nSendo:\nM-matutino, V-vespertino ou N-noturno\n').lower()

if turno == 'm':
    print('Bom Dia!')
elif turno == 'v':
    print('Boa tarde!')
elif turno == 'n':
    print('Boa noite!')
else:
    print('Valor Inválido')

#7º Questão
resposta_sim = 0

pergunta1 = input('Telefonou para a vítima ?\n')
pergunta2 = input('Esteve no local do crime ?\n')
pergunta3 = input('Mora perto da vítima ?\n')
pergunta4 = input('Devia para a vítima ?\n')
pergunta5 = input('Trabalhou com a vítima ?\n')

if pergunta1 == 'sim':
    resposta_sim += 1
if pergunta2 == 'sim':
    resposta_sim += 1
if pergunta3 == 'sim':
    resposta_sim += 1
if pergunta4 == 'sim':
    resposta_sim += 1
if pergunta5 == 'sim':
    resposta_sim += 1

if resposta_sim == 5:
    print('Assassino')
elif resposta_sim >= 3:
    print('Cúmplice')
elif resposta_sim == 2:
    print('Suspeito')
else:
    print('Inocente')