# Peça 5 números e exiba a média deles.
from time import sleep

lista= []

while True:
    nota = float(input("Digite a nota: "))
    lista.append(nota)

    print(f"Deseja adicionar mais uma nota? y ou n")
    escolha = input(" ").upper()
    if escolha == "Y" or escolha == "YES":
        continue
    elif escolha == "N" or escolha == "NO":
        break


media = sum(lista)/ len(lista)

print(f"a media das notas: {lista}")
sleep(1)
print(f"É de: {media}" )








