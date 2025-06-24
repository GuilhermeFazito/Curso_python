# Crie um sistema que pergunta a senha e só permite acesso se estiver correta.
senha = []
usuario = []
def criar_senha():
    criar_senha = input("digite sua senha: ")
    senha.append(criar_senha)

def criar_usuario():
    criar_usuario = input("digite seu usuario: ")
    usuario.append(criar_usuario)

def validacao():
    while True:
        print(f"""
        Bem vindo ao gerenciador de senhas
            """)
        digitar_senha = input("Para acessar digite sua senha: ")
        digitar_usuario = input ("digite seu usuario")

        if digitar_senha in senha and digitar_usuario in usuario:
            print("Acesso autorizado")
            break     
        else: 
            print("Acesso negado") 
            
            
    
   
    
def main():
    criar_senha()
    criar_usuario()
    validacao()

    print("""
        Bem vindo ao seu gerenciador de senha123

        1) Minhas senhas
        2) Cadastrar nova senha
        3) exit 
        """)


main()







