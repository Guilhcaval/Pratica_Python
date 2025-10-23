num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))

try:
    resultado = num1/num2
    print(resultado)
except ZeroDivisionError:
    print("não existe divisão por zero")
except ValueError:
    print("Digite um valor válido")
finally:
    print("Sempre execute algo")