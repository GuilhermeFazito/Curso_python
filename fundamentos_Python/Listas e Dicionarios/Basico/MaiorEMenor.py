## 1. Crie uma lista com 5 números inteiros e imprima o maior e o menor valor.
lista = []
contagem = 0

while contagem < 5: 
    numero = int(input("digite um numero"))
    lista.append(numero)
    contagem += 1

print (f"""
===================================       
O maior numero é: {max(lista)}        
O menor numero é: {min(lista)}
===================================       
""")
