from modulo1 import *
from modulo2 import *

#
def menuModulos():
    formataTitulo(" Nível- code.Academy ")
    menu = """
1 – Básico.
2 – Intermediário.
0 – Voltar.
    """
    print(menu)


def executarModulos():
    x = ""
    while x != "0":
        limpaTela()
        menuModulos()
        x = input("Escolha um nível a ser estudado: ")
        if x == "1":
            limpaTela()
            executarModulo1()
        elif x == "2":
            limpaTela()
            executarModulo2()
        elif x == "0":
            break
        else:
            print("Opção inválida")