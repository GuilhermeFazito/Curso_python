# Peça nome completo e mostre só o primeiro nome.

nome, sobrenome, resto_nome = list(map(str,input("Digite seu nome: ").split(" ")))

print(f"Ola {nome}, como você esta?")