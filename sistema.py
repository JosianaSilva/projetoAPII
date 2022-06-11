from Menus import *
from Usuario import *
from CadastroUsuarios import *
from Forum import main_forum_menu
from Wiki import *
from Quiz import *
from Configuracoes import executaConfig
from functions import *
from menuModulos import *


def autentica(username,password):  
    if(cad.procurarUsuario(username)):
        if(hash_(password) == cad.getSenha(username)):
            return True
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado!")
    return False

def usuarioLogado(username):
    try:
        usuario = cad.getUsuario(username)
        return usuario
    except:
        raise Exception("Erro! Não foi possível recuperar os dados do usuário.")

def loginAutorizado(usuario):
    msg = "Bem-vinda(o) de volta, [blue]"+ usuario.nome + "!"
    print(Panel.fit(msg))
    limpaTela_(2)
    menu_inicial()
    nivel_2 = input()
    if(nivel_2=="1"): #Wiki
        executaWiki(usuario)
        loginAutorizado(usuario)
    elif(nivel_2=="2"):
        execultarModulos()
        loginAutorizado(usuario)
    elif(nivel_2=="3"):
        main_forum_menu()
        loginAutorizado(usuario)
    elif(nivel_2=="4"):
        MenuQuizWorks()
        loginAutorizado(usuario)
    elif(nivel_2=="5"):
        executaConfig(usuario)
        loginAutorizado(usuario)
    elif(nivel_2=="X"): #Opção de sair
        principal()
        print("Saindo...")
    else:
        msgErro("Opção inválida!")
        loginAutorizado(usuario)

def principal():
    limpaTela()
    menu()
    nivel_1 = input()
    
    if(nivel_1 == "1"): #Opção de Login
        def login(): 
            limpaTela()
            formataTitulo(" Login ")
            username = input("\nUsuário: ")
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
        formataTitulo(" Área de cadastro ")
        # cad.mostrarUsuariosCadastrados()
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
    elif(nivel_1 == "X"):
        print("Encerrando...")
        sleep(3)
    else:
        msgErro("Opção inválida!")
        principal()

cad = cadastroUsuario("cadastroUsuarios.db")
principal()
limpaTela_(1)