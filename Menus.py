def menu_inicial():
    print("""
 =======================
|    code.Academy       |
 =======================
    """)
    print("1.Wiki")
    print("2.Módulos")
    print("3.Fórum")
    print("4.Quiz")
    print("5.Configurações da conta")
    print("\n Digite q para sair.")
    
def menu():
    print("""
 =======================
|    code.Academy       |
 =======================
    """)
    print("1.Login")
    print("2.Cadastro para novos usuários")
    print("\n Digite q para sair.")


def MenuWiki():
    menu = """
\tWiki - code.Academy\n 
1. Ver termos
2. Procurar termo
3. Voltar
    """ 
    print(menu)

def menuConfig1():
    menu = """
    --- Configurações ---
    1. Mostrar Perfil
    2. Atualizar 
    3. Voltar
    """
    print(menu)

def menuConfig2():
   menu = """
   --- Configurações ---
   
   O que pretende atualizar?
   1. Nome
   2. Email
   3. Senha
   4. Voltar
   """
   print(menu)