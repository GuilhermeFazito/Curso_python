# Use and para verificar se dois números são maiores que 10.

numero1= int(input("Digite o primeiro numero: "))
numero2= int(input("Digite o segundo numero: "))

verificar= numero1 and numero2 > 10

print(f"{numero1} e {numero2} sao maiores que 10? {verificar}")
