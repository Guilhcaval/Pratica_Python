def funcoes_bolsa(acao):
    valor_recebido = acao
    if acao > 150.99:
        print(f"Ação esta cara! Compre com cuidado!")
    else:
        print("Ação está barata! Aproveite com caltela!")