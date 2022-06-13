from functions import *

def menu_inicial():
    formataTitulo(" code.Academy ")
    menu = """
    [bold #7B68EE]1.[/] Wiki
    [bold #7B68EE]2.[/] Módulos
    [bold #7B68EE]3.[/] Fórum
    [bold #7B68EE]4.[/] Quiz
    [bold #7B68EE]5.[/] Configurações da conta
    [bold #7B68EE]X.[/] Sair
    """
    console.print(menu)
    
def menu():
    formataTitulo(" code.Academy ")
    menu = """
    [bold blue]1.[/] Login
    [bold blue]2.[/] Cadastro para novos usuários
    [bold blue]X.[/] Sair 
    """
    console.print(menu)


def MenuWiki():
    formataTitulo(" Wiki - code.Academy ")
    menu = """
    [bold SeaGreen]1.[/] Ver termos
    [bold SeaGreen]2.[/] Procurar termo
    [bold SeaGreen]3.[/] Voltar
    """ 
    console.print(menu)

def menuConfig1():
    formataTitulo(" Configurações ")
    menu = """
    [bold blue]1.[/] Mostrar Perfil
    [bold blue]2.[/] Atualizar 
    [bold blue]3.[/] Apagar conta
    [bold blue]4.[/] Voltar
    """
    print(menu)

def menuConfig2():
    formataTitulo(" Configurações ")
    menu = """
    O que pretende atualizar?
    [bold blue]1.[/] Nome
    [bold blue]2.[/] Email
    [bold blue]3.[/] Senha
    [bold blue]4.[/] Voltar
    """
    print(menu)