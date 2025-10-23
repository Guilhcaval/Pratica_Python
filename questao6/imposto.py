def calcular_imposto(valor):
    calcular = valor * 0.15
    total = calcular + valor

    return total


valor = float(input("Digite o valor do produto que deseja: "))


total_pruduto = calcular_imposto(valor)

print(f"O valor total do produto é: {total_pruduto}")