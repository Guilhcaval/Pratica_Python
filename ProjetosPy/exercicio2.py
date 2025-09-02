# Questão 1 (Básico)

contador = 0   # inicializa contador

while (contador <= 100):  
    print(f"{contador}")  # imprime o valor do contador
    contador += 1         # incrementa +1 a cada repetição


# Questão 2 (Básico)

contador = 0   # inicializa contador
num = int(input("Digite um Número: ")) 

while(contador <= num):   # executa até o contador ser igual ao número digitado
    print(f"{contador}")  
    contador += 1         # incrementa a cada loop


# Questão 3 (Básico)

print("Operação - Adição")

num1 = int(input("Digite um número: ")) 
num2 = int(input("Digite outro número: ")) 

soma = num1 + num2   # operação de soma

print(f"{num1} + {num2} = {soma}") 

pergunta = input("Deseja realizar outra soma? [S ou N]\n").upper() 

while(True):  # laço infinito até o usuário parar
    if pergunta in 's':  # se a resposta for S
        num1 = int(input("Digite um número: ")) 
        num2 = int(input("Digite outro número: ")) 

        soma = num1 + num2  # soma novamente
        print(f"{num1} + {num2} = {soma}")  # mostra resultado

        pergunta = input("Deseja realizar outra soma? [S ou N]\n").upper()  # pergunta novamente
        
    else:  # se for N
        print(f"Resposta: {pergunta}")  # exibe a resposta
        break  # interrompe o loop


# Questão 1 (Desafio)

a, b = 0, 1   # primeiros valores da sequência de Fibonacci

print("Série de Fibonacci: ")

while True: 
    print(a)  # imprime o valor atual
    if a > 500:  # condição de parada
        break
    a, b = b, a + b  # lógica da sequência de Fibonacci


# Questão 2 (Desafio)

valores = []  # lista para armazenar os números
quant = int(input("Digite a quantidade de números: "))  # quantidade de entradas

for i in range(quant):  # repete até a quantidade informada
    num = int(input("Digite um valor: "))  # lê o valor
    valores.append(num)  # adiciona à lista

maior = menor = valores[0]  # inicializa maior e menor com o primeiro valor

for x in valores:  # percorre todos os valores
    if x > maior:
        maior = x
    if x < menor:
        menor = x

soma = maior + menor  # soma o maior e menor

print("Maior:", maior)
print("Menor:", menor)
print("Soma:", soma)


# Questão 3 (Desafio)

valores = []  
quant = int(input("Digite a quantidade de N números para saber qual é maior, menor e a soma deles: "))
repeticao = 1  # contador de repetição

while repeticao <= quant:  # enquanto não atingir a quantidade desejada
    for i in range(quant):  # percorre a quantidade
        num = int(input("Digite um valor entre 0 e 1000: "))  # validação dos números
    
        if num >= 0 and num <= 1000:  # só aceita dentro do intervalo
            valores.append(num)  # adiciona na lista
            repeticao += 1  # soma repetição
            break  # sai do for e volta pro while
        else:
            print("O número digitado deve ser entre 0 e 1000: ")
        
maior = menor = valores[0]  # define primeiro valor como base
    
for x in valores [0:]:  # percorre lista
    
    if x > maior:
        maior = x
    if x < menor:
        menor = x

soma = maior + menor  # soma do maior e menor

print("maior", maior)
print("menor", menor)
print("soma", soma)


# Questão 4 (Desafio)

# Validação do Nome
nome = input("Digite seu nome: ")
while len(nome) <= 3:  # nome precisa ter mais de 3 caracteres
    nome = input("Nome inválido! Digite um nome com mais de 3 caracteres: ")

# Validação da Idade
idade = int(input("Digite sua idade: "))
while idade < 0 or idade > 150:  # idade só pode estar entre 0 e 150
    idade = int(input("Idade inválida! Digite uma idade entre 0 e 150: "))

# Validação do Salário
salario = float(input("Digite seu salário: "))
while salario <= 0:  # salário não pode ser 0 ou negativo
    salario = float(input("Salário inválido! Digite um valor maior que 0: "))

# Validação do Sexo
sexo = input("Digite seu sexo ('f' ou 'm'): ").lower()
while sexo != "f" and sexo != "m":  # aceita apenas f ou m
    print("Sexo inválido!")
    sexo = input("Digite seu sexo ('f' ou 'm'): ").lower()

# Validação do Estado Civil
estado_civil = input("Digite seu estado civil ('s', 'c', 'v', 'd'): ").lower()
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":  
    # só aceita valores válidos
    print("Estado civil inválido!")
    estado_civil = input("Digite seu estado civil ('s', 'c', 'v', 'd'): ").lower()

# Exibe cadastro finalizado
print("\nCadastro realizado com sucesso!")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")


# Questão 5 (Desafio)

quant = 0  # contador de divisores

num = int(input("Digite um número inteiro: "))  # entrada do número

if num <= 1:  # condição para valores inválidos
    print("Número inválido")
else:
    for contador in range (1, (num + 1)):  # verifica de 1 até o número
        if num % contador == 0:  # se o resto for 0 é divisor
            quant += 1  # soma quantidade de divisores

if quant == 2:  # só 2 divisores = número primo
    print(f"{num} é primo")
if quant > 2:  # mais de 2 divisores = não é primo
    print(f"{num} não é primo")

