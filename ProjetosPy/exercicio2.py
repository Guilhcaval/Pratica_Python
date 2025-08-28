# Questão 1 (Básico)
'''contador = 0

while (contador <= 100):
    print(f"{contador}")
    contador += 1'''

# Questão 2 (Básico)
'''contador = 0
num = int(input("Digite um Número: "))

while(contador <= num):
    print(f"{contador}")
    contador += 1'''

# Questão 3 (Básico)
'''print("Operação - Adição")

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

soma = num1 + num2

print(f"{num1} + {num2} = {soma}")

pergunta = input("Deseja realizar outra soma? [S ou N]\n").upper()

while(True):
    if pergunta in 's':
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))

        soma = num1 + num2
        print(f"{num1} + {num2} = {soma}")

        pergunta = input("Deseja realizar outra soma? [S ou N]\n").upper()
        

    else:
        print(f"Resposta: {pergunta}")
        break'''

#Questão 







# Questão 5 (Desafio)
quant = 0

num = int(input("Digite um número inteiro: "))

if num <= 1:
    print("Número inválido")
else:
    for contador in range (1, (num + 1)):
        if num % contador == 0:
            quant += 1

if quant == 2:
    print(f"{num} é primo")
if quant > 2:
    print(f"{num} não é primo")

