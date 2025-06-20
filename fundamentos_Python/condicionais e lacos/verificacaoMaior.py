# Peça dois números e mostre o maior.

numero1 = int(input("Digite um numero: "))
numero2= int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print(f"O numero {numero1} é maior que {numero2}")
elif numero1 == numero2:
    print(f"Os dois numeros são iguais")
else:
    print(f"O Numero {numero1} é menor que o numero {numero2} ")


