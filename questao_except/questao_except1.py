def operacao(valor1, valor2):
    total_operacao = valor1 / valor2
    print(total_operacao)

valor1 = float(input("Digite um n�mero: "))
valor2 = float(input("Digite um n�mero: "))

operacao(valor1, valor2)

print(operacao)

while True:
    try:
        valor1 = float(input("Digite um n�mero: "))
        valor2 = float(input("Digite um n�mero: "))
        total = valor1 / valor2
        print(total)
    except ZeroDivisionError:
        print("Erro! N�o pode dividir por zero!")

    except ValueError: 
        print("Erro! Digite um novo n�mero: ")
        
    continuar = input("Digite continuar ou sair: ")
    if continuar == "sair":
        print("Programa encerrado, volte sempre.")
        break