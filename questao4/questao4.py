from conversor_idade import conversor_idade

while True:
    idade = int(input("Digite sua idade: \n"))
    conversor_idade(idade)
    continuar = input("Digite 'continuar ou sair' para finalizar: ")
    if continuar == 'sair':
        print("Programa Encerrado!")
        break