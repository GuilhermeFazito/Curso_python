# 2. Crie uma lista de números inteiros e remova todos os números pares da lista.

numeros = []

while True:
    print(numeros)
    numero = int(input("Digite um numero para adicionar a lista: "))
    numeros.append(numero)

    exit = input("deseja sair?").lower()
    if exit == "sim" or exit == "s":
        break

for n in numeros:
    if n % 2 != 0:
        numeros.remove(n)

print (numeros)



