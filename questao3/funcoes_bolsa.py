def funcoes_bolsa(acao):
    valor_recebido = acao
    if acao > 150.99:
        print(f"A��o esta cara! Compre com cuidado!")
    else:
        print("A��o est� barata! Aproveite com caltela!")