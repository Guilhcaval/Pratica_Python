from  conversor import conversor_valor

valor_produto = float(input("Digite o valor do produto: "))
juros_produto = float(input("Digite a '%' do produto: " ))

valor = conversor_valor(valor_produto, juros_produto)

print(f"O valor toral da sua compra é: {valor + valor_produto}")