from modulo1 import *
from modulo2 import *

def menuModulos():
    menu = """\033[91m
   -- Nivel- code.Academy --\033[0m\n
1 – Básico
2 – Intermediário
3 – Avançado
0 – Voltar
    """
    print(menu)

def execultarModulos():
    x = ""
    while x != "0":
        limpaTela()
        menuModulos()
        x = input("Escolha um nível á ser estudado: ")
        limpaTela()
        if x == "1":
           execultarModulo1()
        elif x == "2":
            execultarModulo2()
        elif x == "0":
            break
        else:
            print("opção invalida")