# Verifique se uma palavra é um palíndromo.]

palavra = input("Digite uma palavra")


if palavra == palavra[::-1]:
    print(f"A palavra {palavra} é um palindromo.")
else:
    print(f"A palavra {palavra} não é um palindromo.")

