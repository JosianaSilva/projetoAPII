from Menus import *
from Usuario import *
from CadastroUsuarios import *
from Forum import *
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
    limpaTela()
    msg = "Bem-vinda(o) de volta, [blue]"+ usuario.nome + "!"
    print(Panel.fit(msg))
    limpaTela_(1)
    menu_inicial()
    nivel_2 = input().upper()
    if(nivel_2=="1"): #Wiki
        executaWiki(usuario)
        loginAutorizado(usuario)
    elif(nivel_2=="2"):
        limpaTela()
        executarModulos()
        loginAutorizado(usuario)
    elif(nivel_2=="3"):
        limpaTela()
        main_forum_menu(usuario)
        loginAutorizado(usuario)
    elif(nivel_2=="4"):
        MenuQuizWorks(usuario)
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
    # cad.mostrarUsuariosCadastrados()
    nivel_1 = input().upper()
    
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
limpaTela()