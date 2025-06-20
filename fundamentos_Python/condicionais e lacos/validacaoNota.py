# Peça uma nota de 0 a 10 e valide a entrada com while.
nota = int(input("Digite a nota: "))

while nota < 0 or nota > 10:
    nota = int(input("Nota invalida, digite novamente: ")) 
if nota >= 0 or nota <= 10:
    print(f"Sua nota é {nota}")



