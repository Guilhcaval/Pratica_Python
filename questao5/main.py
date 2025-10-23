from imc import calcular_imc
from classicacao_imc import classificacao

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

resultado = calcular_imc(peso, altura)
classificacao(resultado)    