while True:
    try:
        numero = float(input("Digite um n�mero: "))
        print(f"O numero digitado �: {numero}")

    except ValueError:
        print("Erro! Digite um numero!")