#Peça uma frase e conte quantas vogais tem.

vogais = ["A","E","I","O","U"]
frase = input("Digite uma frase: ").upper()

contador = 0

for letra in frase:
    if letra in vogais:
        contador +=1

print(f"{contador}")
