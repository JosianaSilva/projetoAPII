from perguntas import *
from functions import *

opcao = ""

def menuCapitulos2():
    menu = """
\t--2º Módulo- code.Academy--\n 
1 – Funções
2 – Lista
3 – Matriz
4 – Programação Orientada á Objetos
0 – Voltar
    """ 
    print(menu)


def ler_funcoes(opcao):
    def abrirArquivo(caminho, opcao):
        with open (caminho,"r", encoding="utf-8") as arquivo:
            tx = arquivo.readlines()
            print("".join(map(str, tx[0:29])))
            while opcao != "n":
                opcao = input("CONTINUAR ESTUDANDO? (s/n): ")
                if opcao == "s":
                    limpaTela()
                    print("".join(map(str, tx[29:59])))
                    break
            while opcao != "n":
                opcao = input("VAMOS TESTAR SEU CONHECIMENTO? (s/n): ")
                if opcao == "s":
                    limpaTela() 
                    pergunta_funcoes(perguntas5, certas)
                    break
        arquivo.close
    try:
        abrirArquivo("arquivos/ModArquivos/Funções.txt", opcao)
    except:
        abrirArquivo(r"arquivos\\ModArquivos\\Funções.txt", opcao)


def ler_listas(opcao):
    def abrirArquivo(caminho, opcao):
        with open (caminho,"r", encoding="utf-8") as arquivo:
            tx = arquivo.readlines()
            print("".join(map(str, tx[0:29])))
            while opcao != "n":
                opcao = input("CONTINUAR ESTUDANDO? (s/n): ")
                if opcao == "s":
                    limpaTela()
                    print("".join(map(str, tx[30:60])))
                    break
            while opcao != "n":
                opcao = input("VAMOS TESTAR SEU CONHECIMENTO? (s/n): ") 
                if opcao == "s":
                    limpaTela()
                    pergunta_listas(perguntas6, certas)
                    break
        arquivo.close  
    try:
        abrirArquivo("arquivos/ModArquivos/Listas.txt", opcao)
    except:
        abrirArquivo(r"arquivos\\ModArquivos\\Listas.txt", opcao)

def ler_matriz(opcao):
    def abrirArquivo(caminho, opcao):
        with open (caminho,"r", encoding="utf-8") as arquivo:
            tx = arquivo.readlines()
            print("".join(map(str, tx[0:29])))
            while opcao != "n":
                opcao = input("CONTINUAR ESTUDANDO? (s/n): ")
                if opcao == "s":
                    limpaTela()
                    print("".join(map(str, tx[30:60])))
                    break
            while opcao != "n":
                opcao = input("VAMOS TESTAR SEU CONHECIMENTO? (s/n): ") 
                if opcao == "s":
                    limpaTela()
                    pergunta_matriz(perguntas7, certas)
                    break
        arquivo.close
    try:
        abrirArquivo("arquivos/ModArquivos/Matriz.txt", opcao)
    except:
        abrirArquivo(r"arquivos\\ModArquivos\\Matriz.txt", opcao)


def ler_POO(opcao):
    def abrirArquivo(caminho, opcao):
        with open (caminho,"r", encoding="utf-8") as arquivo:
            tx = arquivo.readlines()
            print("".join(map(str, tx[0:32])))
            while opcao != "n":
                opcao = input("CONTINUAR ESTUDANDO? (s/n): ")
                if opcao == "s":
                    limpaTela()
                    print("".join(map(str, tx[34:61])))
                    break
            while opcao != "n":
                opcao = input("VAMOS TESTAR SEU CONHECIMENTO? (s/n): ")
                if opcao == "s":
                    limpaTela()
                    pergunta_POO(perguntas8, certas)
                    break
        arquivo.close
    try:
        abrirArquivo("arquivos/ModArquivos/POO.txt", opcao)
    except:
        abrirArquivo(r"arquivos\\ModArquivos\\POO.txt", opcao)


def executarModulo2():
    x = ""
    while x != "0":
        limpaTela()
        menuCapitulos2()
        x = input("Digite uma opção desejada: ")
        if x == "1":
            limpaTela()
            ler_funcoes(opcao) 
        elif x == "2":
            limpaTela()
            ler_listas(opcao) 
        elif x == "3":
            limpaTela()
            ler_matriz(opcao)
        elif x == "4":
            limpaTela()
            ler_POO(opcao)
        elif x == "0":
            break
        else:
            print("Opção inválida")