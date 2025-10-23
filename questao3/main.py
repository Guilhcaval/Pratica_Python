from funcoes_bolsa import funcoes_bolsa

while  True:
    acao = float(input("Digite um valor: "))
    funcoes_bolsa(acao)
    continuar = input("Digite 'continuar' ou 'sair' para finalizar: ")
    if continuar == 'sair':
        break