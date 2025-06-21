# Mostre todos os números pares de 1 a 50.
from time import sleep
pares = []
impar = []


for numero in range(1, 101):
    if (numero % 2) == 0:
        pares.append(numero)
    else:
        impar.append(numero)
    

print(f"Numeros pares: {pares} ")
sleep(1)
print(f"Numeros impar: {impar}")
