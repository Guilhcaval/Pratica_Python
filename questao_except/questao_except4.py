def dividir (a,b):
    divisao_valor = a / b
    return divisao_valor

try: 
    a = float(input("Digite um valor: "))
    b = float(input("Digite um valor: "))

    total_divisao = dividir(a,b)
    
    print(f"Resultdo da divisão: {total_divisao:.1F}")
except ZeroDivisionError:
    print("Erro! Não pode ser dividido por ZERO, cabeça!")