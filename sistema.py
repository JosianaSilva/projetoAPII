from Menus import *
from Usuario import *
from CadastroUsuarios import *
from Wiki import *
from time import sleep
import os


from Wiki import executaWiki
op = "0"
op2 = "0"

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def autentica(user,password):  
    if(user != "") and (password != ""):
        teste = True
    else:
        teste = False
    return teste

def wiki():
    print("Em produção...")

while(op!="q"):
    limpaTela()
    menu_login()
    op1 = input()
    if(op1 == "1"): #Opção de Login
        limpaTela()
        user = input("Usuário: ")
        password = input("Senha: ")

        logado = autentica(user,password)
        limpaTela()

        if logado:
            menu_inicial()
            op2 = input()

            if(op2=="1"): #Wiki
                executaWiki()
                op2 = "0"
            elif(op2=="q"): #Opção de sair
                logado = False
            else:
                print("Em desenvolvimento...")
                sleep(2)
        else:
            print("Erro!")
    
    elif (op1 == "2"): #Opção de Cadastro de novos usuários
        limpaTela()
        novo = cadastroUsuario()
        print("Novo usuário:", novo.nome)
        continuar = input("Gostaria de fazer login? (s/n)")
        if(continuar == "s"):
            op1 = 1
        else:
            op = "q"
    elif(op1 == "q"):
        op = "q"
    else:
        op =  input()
limpaTela()
print("Encerrando...")