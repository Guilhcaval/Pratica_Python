while True:
    try:
        valor1 = float(input("Digite um n�mero: "))
        valor2 = float(input("Digite um n�mero: "))
        total =  valor1 / valor2
        print(total)
    except ZeroDivisionError:
        print("Erro! N�o pode dividir por zero!")

    except ValueError: 
        print("Erro! Digite um novo n�mero: ")