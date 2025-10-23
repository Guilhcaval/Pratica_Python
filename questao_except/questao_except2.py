while True:
    try:
        numero = float(input("Digite um número: "))
        print(f"O numero digitado é: {numero}")

    except ValueError:
        print("Erro! Digite um numero!")