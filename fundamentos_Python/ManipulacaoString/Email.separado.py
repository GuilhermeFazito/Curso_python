#Peça um e-mail e separe o nome do usuário do domínio.
print("Seu nome de usuario sera o nome do email anterior ao '@' !")
nome, dominio = list(map(str,input("Digite seu Email: ").split("@")))

print(f"Nome de usuario: {nome}")
print(f"Dominio do Email: {dominio}")