# 1. Crie um dicionário de produtos, onde a chave seja o nome do produto e o valor seja o preço. 
# Permita que o usuário consulte o preço de um produto digitando seu nome.


produtos = {}


#Adicionar produtos para o usuario
while True:
    nome = input("Digite o nome do Produto (ou SAIR):").title()
    if nome == "Sair":
        break

    preco = float(input(f"Digite o preço do produto '{nome}': "))
    validade = input("Digite a validade do produto: ")

    produtos[nome] = {
        "preco": preco,
        "validade": validade
    }

#Verificar o preço do produto pelo nome

verificar = input("Qual o produto que deseja verificar o preço? ").title()

while True:
    if verificar in produtos:
        print(f"""
=== Detalhes do Produto ===
 Nome     : {verificar}
 Preço    : R$ {produtos[verificar]['preco']:.2f}
 Validade : {produtos[verificar]['validade']}
============================""")
        break                                                                                           
    else:
        print("nome invalido, tente novamente")
