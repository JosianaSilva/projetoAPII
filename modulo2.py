from perguntas import *
from functions import *

opcao = ""

# Função para exibir o menu:
def menuCapitulos2():                   
    formataTitulo(" 2º Módulo- code.Academy ")
    menu = """
1 – Funções.
2 – Lista.
3 – Matriz.
4 – Programação Orientada á Objetos.
0 – Voltar.
    """ 
    print(menu)

# Função leitura de "arquivos.txt"
def ler_funcoes(opcao):                                             #Recebe como parametro á variável opcao.
    def abrirArquivo(caminho, opcao):                               #Função usada para escolher o caminho do diretório apartir do seu SO.
        with open (caminho,"r", encoding="utf-8") as arquivo:       #Recebe o dirétorio apartir do objeto "caminho", para leitura.
            tx = arquivo.readlines()                                #Adiciona o arquivo em uma #Recebe como parametro á variável opcao.lista para manipulação.
            print("".join(map(str, tx[0:29])))                      #Imprime na tela o arquivo já manipulado do indíce 0 ao 29.
            while opcao != "n":
                opcao = input("\033[93mCONTINUAR ESTUDANDO? (s/n): \033[0m")   #Laço criado para que o usuario possa continuar estudando ou não. 
                if opcao == "s":
                    limpaTela()
                    print("".join(map(str, tx[29:59])))             #Imprime na tela o arquivo já manipulado do indíce 29 ao 59.
                    break
            while opcao != "n":
                opcao = input("\033[93mVAMOS TESTAR SEU CONHECIMENTO? (s/n): \033[0m")     #Laço criado para que o usuário possa responde ao teste de conhecimento ou não.
                if opcao == "s":
                    limpaTela() 
                    pergunta_funcoes(perguntas5, certas)            #Chama a função que mostra as perguntas referentes ao capítulo.
                    break
        arquivo.close
    try:
        abrirArquivo("arquivos/ModArquivos/Funções.txt", opcao)     #Diretório Linux\Mac.
    except:
        abrirArquivo(r"arquivos\\ModArquivos\\Funções.txt", opcao)  #Diretório Windows.

# Função leitura de "arquivos.txt"
def ler_listas(opcao):
    def abrirArquivo(caminho, opcao):                               #Comportamento igual á anterior.
        with open (caminho,"r", encoding="utf-8") as arquivo:
            tx = arquivo.readlines()
            print("".join(map(str, tx[0:29])))
            while opcao != "n":
                opcao = input("\033[93mCONTINUAR ESTUDANDO? (s/n): \033[0m")
                if opcao == "s":
                    limpaTela()
                    print("".join(map(str, tx[30:60])))
                    break
            while opcao != "n":
                opcao = input("\033[93mVAMOS TESTAR SEU CONHECIMENTO? (s/n): \033[0m") 
                if opcao == "s":
                    limpaTela()
                    pergunta_listas(perguntas6, certas)
                    break
        arquivo.close  
    try:
        abrirArquivo("arquivos/ModArquivos/Listas.txt", opcao)      #Diretório Linux\Mac.
    except:
        abrirArquivo(r"arquivos\\ModArquivos\\Listas.txt", opcao)   #Diretório Windows.

# Função leitura de "arquivos.txt"
def ler_matriz(opcao):
    def abrirArquivo(caminho, opcao):                               #Comportamento igual á anterior.
        with open (caminho,"r", encoding="utf-8") as arquivo:
            tx = arquivo.readlines()
            print("".join(map(str, tx[0:29])))
            while opcao != "n":
                opcao = input("\033[93mCONTINUAR ESTUDANDO? (s/n): \033[0m")
                if opcao == "s":
                    limpaTela()
                    print("".join(map(str, tx[30:60])))
                    break
            while opcao != "n":
                opcao = input("\033[93mVAMOS TESTAR SEU CONHECIMENTO? (s/n): \033[0m") 
                if opcao == "s":
                    limpaTela()
                    pergunta_matriz(perguntas7, certas)
                    break
        arquivo.close
    try:
        abrirArquivo("arquivos/ModArquivos/Matriz.txt", opcao)      #Diretório Linux\Mac.
    except:
        abrirArquivo(r"arquivos\\ModArquivos\\Matriz.txt", opcao)   #Diretório Windows.

# Função leitura de "arquivos.txt"
def ler_POO(opcao):
    def abrirArquivo(caminho, opcao):                               #Comportamento igual á anterior.
        with open (caminho,"r", encoding="utf-8") as arquivo:
            tx = arquivo.readlines()
            print("".join(map(str, tx[0:32])))
            while opcao != "n":
                opcao = input("\033[93mCONTINUAR ESTUDANDO? (s/n): \033[0m")
                if opcao == "s":
                    limpaTela()
                    print("".join(map(str, tx[34:64])))
                    break
            while opcao != "n":
                opcao = input("\033[93mVAMOS TESTAR SEU CONHECIMENTO? (s/n): \033[0m")
                if opcao == "s":
                    limpaTela()
                    pergunta_POO(perguntas8, certas)
                    break
        arquivo.close
    try:
        abrirArquivo("arquivos/ModArquivos/POO.txt", opcao)     #Diretório Linux\Mac.
    except:
        abrirArquivo(r"arquivos\\ModArquivos\\POO.txt", opcao)  #Diretório Windows.


def executarModulo2():
    x = ""
    while x != "0":
        limpaTela()
        menuCapitulos2()    #Mostra as opções do menu
        x = input("Digite uma opção desejada: ")
        if x == "1":
            limpaTela()
            ler_funcoes(opcao)  #executa a função de leitura.
        elif x == "2":
            limpaTela()
            ler_listas(opcao)   #executa a função de leitura.
        elif x == "3":
            limpaTela()
            ler_matriz(opcao)   #executa a função de leitura.
        elif x == "4":
            limpaTela()
            ler_POO(opcao)      #executa a função de leitura.
        elif x == "0":
            break               #Encerra o laço e volta ao passo anterior.
        else:
            print("Opção inválida")
        continua()