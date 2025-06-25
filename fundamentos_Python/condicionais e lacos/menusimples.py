# Implemente um menu simples com while e if.


from random import choice
import sys


while True:
    print("""
        ========================================
                    Bem-vindo ao 
                Pedra, papel ou tesoura         
        ========================================
        Escolha uma das opçoes:
        1) Jogar
        2) Ver Regras
        3) Sair
        ========================================
        """)
    escolha = int(input("Escreva a opção: "))

    while True:
    
        if escolha == 1:
            print(""" 
            ============================
                Bem vindo ao jogo
            ============================
            """) 
            print(""" 
            Escolha entre:
            Pedra
            Papel
            Tesoura
            """)
            opcoes = ["Pedra", "Papel", "Tesoura"]
            escolha_bot = choice(opcoes).upper()
            
            while True:
                acao = str(input("digite sua escolha: ").upper())
            
            
                # Player escolhe igual a maquina
                if acao == escolha_bot:
                    print(f""" 
    ========================================      
            Voce EMPATOU!
    Sua escolha foi: {acao} 
    A maquina escolheu: {escolha_bot}
    ========================================  
                        """)
                    break
                    
                #Player escolhe pedra
                elif acao == "PEDRA":
                    if escolha_bot == "PAPEL":
                        print(f"""       
    ========================================      
            Voce Perdeu!
    Sua escolha foi: {acao} 
    A maquina escolheu: {escolha_bot}
    ========================================    
                        """)
                        break
                    elif escolha_bot == "TESOURA":
                        print(f"""        
    ========================================      
            Voce Ganhou!
    Sua escolha foi: {acao} 
    A maquina escolheu: {escolha_bot}
    ========================================    
                        """)
                        break
                
                #Player escolhe papel
                elif acao == "PAPEL":
                    if escolha_bot == "TESOURA":
                        print(f"""        
    ========================================      
            Voce Perdeu!
    Sua escolha foi: {acao} 
    A maquina escolheu: {escolha_bot}
    ========================================    
                        """)
                        break
                    elif escolha_bot == "PEDRA":
                        print(f"""        
    ========================================      
            Voce Ganhou!
    Sua escolha foi: {acao} 
    A maquina escolheu: {escolha_bot}
    ========================================    
                        """)
                        break
                
                #Player escolhe TESOURA
                elif acao == "TESOURA":
                    if escolha_bot == "PEDRA":
                        print(f"""  
    ========================================      
            Voce Perdeu!
    Sua escolha foi: {acao} 
    A maquina escolheu: {escolha_bot}
    ========================================    
                        """)
                        break
                    elif escolha_bot == "PAPEL":
                        print(f"""        
    ========================================      
            Voce Ganhou!
    Sua escolha foi: {acao} 
    A maquina escolheu: {escolha_bot}
    ========================================    
                        """)
                        break
            print("voce deseja jogar novamente? SIM ou NÂO")
            escolha_continuar = input("Digite aqui: ").upper()
            if escolha_continuar == "SIM" or escolha_continuar == "S":
                continue
            elif escolha_continuar == "NÃO" or escolha_continuar == "N" or escolha_continuar == "NAO":
                break




        #Caso usuario escolha acessar as regras        
        elif escolha == 2:
            print("""
=======================================
        REGRAS
PEDRA ganha de TESOURA
TESOURA ganha de PAPEL
PAPEL ganha de pedra
=======================================                     
                """)
            print("Deseja retornar ao menu? ")

            retornar_menu = input("Digite aqui: ") .upper()
            if retornar_menu == "SIM" or retornar_menu == "S":
                break

        
        elif escolha == 3:
            print("Fechando o Programa")
            sys.exit()
                

        
        





            
            

            
       



