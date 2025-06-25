# Verifique se uma palavra existe dentro de uma frase.

frase = list(map(str,input("Digite uma frase: ").split(" ")))
palavra = input("Digite uma palavra")

if palavra in frase:
    print(f"A palavra {palavra} esta na frase")
else:
    print(f"A palavra {palavra} não esta na frase")