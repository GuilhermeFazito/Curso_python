# Peça um número e diga se é par ou ímpar.

numero1 = int(input("digite um numero "))

calculo = (numero1 % 2)

if calculo == 0:
    print(f"{numero1} é um numero par")
else:
    print(f"{numero1} é um numero impar")