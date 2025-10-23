def calcular_imc(peso, altura):
    
    imc = peso / (altura ** 2)
    print(f"Seu IMC é: {imc:.2f}")
    return imc