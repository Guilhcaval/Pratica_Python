# QUESTÃO 1
num = int(input("Digite um número: "))
i = 1
for i in range(1, 11):
    multi = i * num
    print(f"{i} * {num} = {multi}")

while i <= 10:
    multi = i * num
    print(f"{i} * {num} = {multi}")
    i+=1

#QUESTÃO 2

usuarios = [
    {"usuario": "admin", "senha": "1234"},
    {"usuario": "joao", "senha": "abcd"},
    {"usuario": "maria", "senha": "4321"},  
]

user = input('Digite o usuario: ')
senha = input('Digite a senha: ')

contador = 0

for i in range(0, 4):
    if user == "usuario" and senha == "senha" :
        print("Login realizado com sucesso!")
        break
    elif user != usuarios or senha != usuarios:
        print('Usuario ou senha inválidos!')   
        contador += 1

    if contador == 4:
        print("Tentativa de Login Bloqueada")



# QUESTÃO 3

nome_digi = input("Digite seu nome: ")
idade_digi = int(input("Digite sua idade: "))
altura_digi = float(input("Digite sua altura: "))
cidade_digi = input("Digite sua cidade: ")


dados ={
    "nome": nome_digi,
    "idade": idade_digi,
    "altura": altura_digi,
    "cidade" : cidade_digi
}


print(f"Nome:",{dados["nome"]})
print(f"Idade:",{dados["idade"]})
print(f"Altura:",{dados["altura"]})
print(f"Cidade:",{dados["cidade"]})