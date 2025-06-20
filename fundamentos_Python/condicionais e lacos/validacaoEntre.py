# Peça um número e diga se está entre 10 e 20.


numero = int(input("digite o numero que esta entre 10 e 20: "))

while numero < 10 or numero > 20:
    print(f"Numero invalido")
    numero = int(input("Digite novamente: "))
if numero >= 10 and numero <= 20:
    print(f"O numero {numero} enta entre 10 e 20")





