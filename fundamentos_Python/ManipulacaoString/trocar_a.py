#Troque todas as letras "a" por "@" em uma frase.

palavra = input("Digite uma palavra: ").upper()
frase = input("digite uma frase").upper()

palavra_reformulada = palavra.replace("A", "@")
frase_reformulada = frase.replace("A", "@")

print(f"{palavra.title()} virou {palavra_reformulada.lower()}")
print(f"{frase.title()} virou {frase_reformulada.lower()}")



