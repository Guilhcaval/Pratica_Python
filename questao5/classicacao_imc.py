def classificacao(imc):
    if 18.5 <= imc <= 24.9:
        print("Peso ideal!")
    elif imc >= 25:
        print("Acima do peso!")
    elif imc < 18.5:
        print("Abaixo do peso!")
    else:
        print("Erro! Retorne ao início.")