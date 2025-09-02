'''
lista_par = []
lista_impar = []


num = int(input("Digite um número inteiro: "))

for contador in range(1, (num + 1)):
    if contador % 2 == 0:
        lista_par.append(contador)
    else:
        lista_impar.append(contador)

print(f"Números pares até {num}: {lista_par}")
print(f"Números ímpares até {num}: {lista_impar}")
'''
'''
num = int(input("Digite um valor inteiro: "))

print(f"O dobro dos números de 1 até {num}:")
for contador in range (1, (num + 1)):
    print(f"{contador}-> {contador * 2}")
'''
'''
print("Bem-vindo ao Conversor de Temperaturas!")

while(True):
    opcao = int(input("Escolha uma opção:\n1. Converter de Celsius para Fahrenheit\n2. Converter de Fahrenheit para Celsius\n3. Sair\n"))
    if opcao == 1:
        cel = float(input("Digite a temperatura em Celsius: "))
        fahrenheit = (cel * 9/5) + 32
        print(f"{cel} graus Celsius é igual a {fahrenheit} graus Fahrenheit")
    elif opcao == 2:
        fah = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = (fah - 32) * 5/9
        print(f"{fah} graus Fahrenheit é igual a {celsius} graus Celsius")
    else:
        print("Saindo...")
        break
'''

