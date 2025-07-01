# 2. Solicite ao usuário 10 números e armazene-os em uma lista. Em seguida, exiba a lista na ordem inversa.

lista = []
contagem = 0

while contagem < 10:
    numero = int(input("Digite o numero: "))
    lista.append(numero)
    contagem += 1

lista.reverse()
print(f"A lista de numero ao inverso é {lista}")
