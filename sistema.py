from menu_inicial import menu_inicial, menu_login
import os
op = "0"
#2
#user = "nulo"
#password = "nulo"
def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def autentica(user,password):  
    if(user != "") and (password != ""):
        teste = True
    else:
        teste = False
    return teste

def cadastroUsuario():
    print("Em produção...")

while(op!="q"):
    limpaTela()
    menu_login()
    op2 = input()
    if(op2 == "1"):
        user = input("Usuário: ")
        password = input("Senha: ")

        logado = autentica(user,password)
        limpaTela()

        if logado:
            menu_inicial()
            op = input()
        else:
            print("Erro!")
    
    elif(op2 == "2"):
        cadastroUsuario()
    op =  input()
limpaTela()
print("Encerrando..")