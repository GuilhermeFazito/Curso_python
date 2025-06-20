#Imprima a tabuada de um número de 1 a 10.]
from time import sleep

while True: 
    numero = int(input("Digite o numero que deseja: "))

    for tabuada in range(0, 11):
        resultado = numero * tabuada
        print(f"{numero} x {tabuada} = {resultado}")
        sleep(0.5)
    print("Você deseja escolher outro numero?")
    
    resposta_return = input("Digite SIM ou NÃO: ").upper() 
    if resposta_return == "SIM":
        print("Retornando")
    elif resposta_return == "NAO" or "NÃO":
        print("Fechando o Programa")
        exit()

