from Menus import *
from Usuario import *
from CadastroUsuarios import *
from Wiki import *
from Quiz import *
from time import sleep
import os
from getpass import getpass
from Wiki import executaWiki

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def hash_(string):
    return hashlib.md5(string.encode()).hexdigest() 

def autentica(user,password):  
    if(cad.procurarUsuario(user)):
        if(hash_(password) == cad.getSenha(user)):
            return True
        else:
            print("senha incorreta")
    else:
        print("Usuário não encontrado")
    return False

def usuarioLogado(user):
    try:
        usuario = cad.getUsuario(user)
        return usuario
    except:
        raise Exception("Erro!")

def loginAutorizado(usuario):
    limpaTela()
    print("Olá, ",usuario.nome,"!")
    menu_inicial()
    nivel_2 = input()
    if(nivel_2=="1"): #Wiki
        executaWiki(usuario)
        loginAutorizado(usuario)
    elif(nivel_2=="2"):
        print("Módulos em desenvolvimento..")
        loginAutorizado(usuario)
    elif(nivel_2=="3"):
        print("Fórum em desenvolvimento..")
        loginAutorizado(usuario)
    elif(nivel_2=="4"):
        MenuQuizWorks()
        loginAutorizado(usuario)
    elif(nivel_2=="q"): #Opção de sair
        principal()
        print("Saindo...")
        sleep(2)

def principal():
    limpaTela()
    menu()
    nivel_1 = input()
    
    if(nivel_1 == "1"): #Opção de Login
        def login(): 
            limpaTela()
            user = input("Usuário: ")
            password = getpass("Senha: ")

            logado = autentica(user,password)

            if logado:
                usuario = usuarioLogado(user)
                
                loginAutorizado(usuario)
            else:
                print("Erro! Usuário ou senha incorretos.")
                sleep(3)
                continuar = input("Gostaria de tentar novamente? (s/n) ")
                if(continuar == "s"):
                    login()
                else:
                    principal()

        login()
    
    elif (nivel_1 == "2"): #Opção de Cadastro de novos usuários
        limpaTela()
        
        cad.mostrarUsuariosCadastrados()
        novo = cad.cadastroUsuario()

        if(cad.procurarUsuario(novo)):
            print(novo.nome, "cadastrado com sucesso!")
            continuar = input("Gostaria de fazer login? (s/n)")
            if(continuar == "s"):
                loginAutorizado(novo)
            else:
                principal()
        else:
            print("Erro no cadastro :(")
            sleep(3)
            principal()
    elif(nivel_1 == "q"):
        print("Encerrando...")
        sleep(5)

cad = cadastroUsuario("cadastroUsuarios.db")
principal()
limpaTela()