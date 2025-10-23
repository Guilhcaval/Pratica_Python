def conversor_valor(valor_produto, juros_produto):
    conversor_porcentagem = juros_produto / 100
    total_valor = valor_produto * conversor_porcentagem

    return total_valor