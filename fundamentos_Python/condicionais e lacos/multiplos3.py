# Conte quantos números entre 1 e 100 são múltiplos de 3.
from time import sleep


multiplos = []
nao_multiplos = []

for number in range(1, 101):
    if (number % 3 ) == 0:
        multiplos.append(number)
    else:
        nao_multiplos.append(number)

print(f"Numeros multiplos de 3: {multiplos}")
sleep(1)
print(f"Numeros não multiplos de 3: {nao_multiplos}")


        
