from functions import *

def menu_inicial():
    formataTitulo(" code.Academy ")
    print("\n 1. Wiki")
    print(" 2. Módulos")
    print(" 3. Fórum")
    print(" 4. Quiz")
    print(" 5. Configurações da conta")
    print(" X. Sair")
    
def menu():
    formataTitulo(" code.Academy ")
    print("\n1. Login")
    print("2. Cadastro para novos usuários")
    print("X. Sair")


def MenuWiki():
    formataTitulo(" Wiki - code.Academy ")
    menu = """
    1. Ver termos
    2. Procurar termo
    3. Voltar
    """ 
    print(menu)

def menuConfig1():
    formataTitulo(" Configurações ")
    menu = """
    1. Mostrar Perfil
    2. Atualizar 
    3. Voltar
    """
    print(menu)

def menuConfig2():
    formataTitulo(" Configurações ")
    menu = """
    O que pretende atualizar?
    1. Nome
    2. Email
    3. Senha
    4. Voltar
    """
    print(menu)