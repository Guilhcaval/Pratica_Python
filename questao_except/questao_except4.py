def dividir (a,b):
    divisao_valor = a / b
    return divisao_valor

try: 
    a = float(input("Digite um valor: "))
    b = float(input("Digite um valor: "))

    total_divisao = dividir(a,b)
    
    print(f"Resultdo da divis�o: {total_divisao:.1F}")
except ZeroDivisionError:
    print("Erro! N�o pode ser dividido por ZERO, cabe�a!")