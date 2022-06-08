from Menus import *
from Usuario import *
from CadastroUsuarios import *
from Wiki import *
from Quiz import *
from Configuracoes import executaConfig
from time import sleep
import os
from getpass import getpass

def limpaTela():
    sleep(1 )
    os.system('cls' if os.name == 'nt' else 'clear')

def hash_(string):
    return hashlib.md5(string.encode()).hexdigest() 

def autentica(username,password):  
    if(cad.procurarUsuario(username)):
        if(hash_(password) == cad.getSenha(username)):
            return True
        else:
            print("senha incorreta")
    else:
        print("Usuário não encontrado")
    return False

def usuarioLogado(username):
    try:
        usuario = cad.getUsuario(username)
        return usuario
    except:
        raise Exception("Erro! Não foi possível recuperar os dados do usuário.")

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
    elif(nivel_2=="5"):
        executaConfig(usuario)
        loginAutorizado(usuario)
    elif(nivel_2=="q"): #Opção de sair
        principal()
        print("Saindo...")

def principal():
    limpaTela()
    menu()
    nivel_1 = input()
    
    if(nivel_1 == "1"): #Opção de Login
        def login(): 
            limpaTela()
            username = input("Usuário: ")
            password = getpass("Senha: ")

            logado = autentica(username,password)

            if logado:
                usuario = usuarioLogado(username)    
                loginAutorizado(usuario)
            else:
                continuar = input("Gostaria de tentar novamente? (s/n) ")
                if(continuar == "s"):
                    login()
                else:
                    principal()
        login()
    
    elif (nivel_1 == "2"): #Opção de Cadastro de novos usuários
        limpaTela()
        print("==== Área de cadastro ====")
        cad.mostrarUsuariosCadastrados()
        novo = cad.cadastroUsuario()

        if(cad.procurarUsuario(novo.nome)):
            print(novo.nome, "cadastrado com sucesso!")
            continuar = input("Gostaria de fazer login? (s/n)")
            if(continuar == "s"):
                loginAutorizado(novo)
            else:
                principal()
        else:
            print("Erro no cadastro :(")
            principal()
    elif(nivel_1 == "q"):
        print("Encerrando...")
        sleep(5)

cad = cadastroUsuario("cadastroUsuarios.db")
principal()
limpaTela()