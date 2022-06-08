from perguntas import *
from functions import *

def menuCapitulos2():
    menu = """
\t--\033[93m2º Módulo- code.Academy--\033[0m\n 
1 – Funções
2 – Lista
3 – Matriz
4 – Programação Orientada á Objetos
0 – Voltar
    """ 
    print(menu)



def execultarModulo2():
    x = ""
    while x != "0":
        menuCapitulos2()
        x = input("Digite uma opção desejada: ")
        if x == "1":
            pass
        elif x == "2":
            pass
        elif x == "3":
            pass
        elif x == "4":
            pass
        elif x == "0":
            break
        else:
            print("Opção Inexistente")
        
    