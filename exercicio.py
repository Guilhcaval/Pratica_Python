# 1º Questão
numero = int(input('Digite um número: '))  # recebe um número inteiro

if numero % 2 == 0:  # verifica se o resto da divisão por 2 é 0
    print('O seu número é par')
else:  # se não for par, é ímpar
    print('O seu número é ímpar')


# 2º Questão
number1 = int(input('Digite um número: '))  # primeiro número
number2 = int(input('Digite outro número: '))  # segundo número

if number1 > number2:  # verifica quem é maior
    print(f'{number1}')
elif number1 == number2:  # se forem iguais
    print('Os números são iguais')
else:  # caso contrário, o segundo é maior
    print(f'{number2}')


# 3º Questão
letra = input('Digite uma letra: ')  # entrada de uma letra

if (letra in 'aeiou'):  # verifica se a letra está na lista de vogais
    print('Vogal')
else:  # caso contrário é consoante
    print('Consoante')


# 4º Questão
nota1 = float(input('Digite a primeira nota: '))  # primeira nota
nota2 = float(input('Digite a segunda nota: '))  # segunda nota

media = (nota1 + nota2)/ 2  # cálculo da média

if media == 10:  # aprovado com nota máxima
    print('Aprovado com Distinção')
elif media >= 7:  # aprovado com média mínima 7
    print('Aprovado')
elif media < 7:  # caso contrário, reprovado
    print('Reprovado')


# 5º Questão
num1 = int(input('Digite um número: '))  # entrada do 1º número
num2 = int(input('Digite um número: '))  # entrada do 2º número
num3 = int(input('Digite um número: '))  # entrada do 3º número

# verifica qual número é maior
if num1 > num2 and num3:
    print(f'{num1}')
elif num2 > num3 and num1:
    print(f'{num2}')
elif num3 > num1 and num2:
    print(f'{num3}')


# 6º Questão
turno = input('Digite o turno no qual você estuda\nSendo:\nM-matutino, V-vespertino ou N-noturno\n').lower()  
# .lower() transforma em minúscula para facilitar comparação

if turno == 'm':  # se for matutino
    print('Bom Dia!')
elif turno == 'v':  # se for vespertino
    print('Boa tarde!')
elif turno == 'n':  # se for noturno
    print('Boa noite!')
else:  # qualquer outro valor é inválido
    print('Valor Inválido')


# 7º Questão
resposta_sim = 0  # contador de respostas "sim"

# perguntas
pergunta1 = input('Telefonou para a vítima ?\n')
pergunta2 = input('Esteve no local do crime ?\n')
pergunta3 = input('Mora perto da vítima ?\n')
pergunta4 = input('Devia para a vítima ?\n')
pergunta5 = input('Trabalhou com a vítima ?\n')

# verifica se cada resposta foi "sim", e soma no contador
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

# classificação baseada no número de respostas "sim"
if resposta_sim == 5:  # respondeu sim a todas
    print('Assassino')
elif resposta_sim >= 3:  # respondeu sim a 3 ou 4
    print('Cúmplice')
elif resposta_sim == 2:  # respondeu sim a 2
    print('Suspeito')
else:  # menos de 2
    print('Inocente')
