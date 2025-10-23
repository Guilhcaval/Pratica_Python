def operacao(valor1, valor2):
    total_operacao = valor1 / valor2
    print(total_operacao)

valor1 = float(input("Digite um número: "))
valor2 = float(input("Digite um número: "))

operacao(valor1, valor2)

print(operacao)

while True:
    try:
        valor1 = float(input("Digite um número: "))
        valor2 = float(input("Digite um número: "))
        total = valor1 / valor2
        print(total)
    except ZeroDivisionError:
        print("Erro! Não pode dividir por zero!")

    except ValueError: 
        print("Erro! Digite um novo número: ")
        
    continuar = input("Digite continuar ou sair: ")
    if continuar == "sair":
        print("Programa encerrado, volte sempre.")
        break