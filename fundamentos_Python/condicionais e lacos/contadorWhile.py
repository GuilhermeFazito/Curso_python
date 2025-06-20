# Faça um contador de 10 até 1 com while.
from time import sleep

number = 10

while number >= 0:
    print(f"{number}")
    number -= 1
    sleep(0.5)