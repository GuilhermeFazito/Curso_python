# Crie um dicionário com as chaves "nome", "idade" e "cidade", preenchendo com seus próprios dados e armazenando em um arquivo JSON.
import os
import json

arquivo_json = "registro.json"

if os.path.exists(arquivo_json):
    with open(arquivo_json, "r", encoding="utf -8") as arquivo:
        registro = json.load(arquivo)
else:
    registro = []







while True:
    pessoa = {}
    pessoa["Nome"] = input("Digite seu nome: ")
    pessoa["Idade"] = int(input("Digite sua idade: "))
    pessoa["Cidade"] = input("Digite sua cidade: ")

    registro.append(pessoa)

    adicionar_mais = input("deseja adicionar mais um nome a sua lista?").upper()
    if adicionar_mais == "SIM" or adicionar_mais == "S":
        continue
    else:
        break


for pessoa in registro :
    print(f"""
Nome: {pessoa["Nome"]},
Idade: {pessoa["Idade"]}
Cidade: {pessoa["Cidade"]}
""")
    

with open(arquivo_json, "w", encoding= "utf -8") as arquivo:
    json.dump(registro, arquivo, indent=4, ensure_ascii=False )

print(f" registros salvos em {arquivo_json}")

   