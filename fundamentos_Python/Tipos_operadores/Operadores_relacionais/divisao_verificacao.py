# Peça dois números e exiba se o primeiro é divisível pelo segundo.

numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

verificacao = ((numero2 % numero1) == 0)

print(f"{numero2} é divisivel por {numero1}? {verificacao}")