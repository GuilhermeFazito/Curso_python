#Peça um número e calcule o fatorial dele.

numero = int(input("Digite um numero: "))
resultado = numero


for fator in range (1, numero):
    resultado *= fator


print(f"O resultado da fatoração do numero {numero} é: {resultado}")