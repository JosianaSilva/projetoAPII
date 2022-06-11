from functions import *
from Menus import menu_inicial
from CadastroUsuarios import *
from Usuario import *

def bem_vindo(usuario):
    limpaTela()
    print(f"Seja bem-vindo(a) ao fórum, {usuario.nome}!")
    sleep(2)
    limpaTela()

def deseja_continuar(x): ##será implementado
    print('Você está indo acessar ' '\033[1m' + x + '\033[0m'+"."' Deseja continuar?')
    desejo = input("s/n")

def menu_inicial_forum():
    print("""Fórum code.Academy
    1. Mostrar postagens
    2. Fazer uma postagem
    3. Procurar postagem
    4. Editar postagem
    4. Sair""")

def cria_tabela_forum():
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
    usuario TEXT NOT NULL PRIMARY KEY,
    titulo TEXT NOT NULL,
    texto TEXT NOT NULL,
    comentarios TEXT
    );
    """)
    banco.commit()
    banco.close()

def novo_post(usuario): #adiciona um post ao banco de dados do fórum
    limpaTela()
    print("Fazer um post:")
    titulo = str(input("Título:\n"))
    texto = input("Texto da postagem:\n")
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    cursor.execute("INSERT OR IGNORE INTO posts (usuario, titulo, texto) VALUES (?,?,?)",(usuario.nome,titulo,texto))
    print("Postado!")               
    banco.commit()
    banco.close()

def ver_posts():
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM posts;")
    print("-"*10) 
    for postagens in cursor.fetchall():
        for formatacao in postagens: 
            print(formatacao)
        print("-"*10)
    banco.close

def editar_post(usuario):
    limpaTela()
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    novo_titulo = input("Novo título:\n")
    novo_texto = input("Novo texto:\n")
    cursor.execute("""UPDATE posts SET titulo = ?, texto = ? WHERE usuario = ?"""
    ,(novo_titulo,novo_texto,usuario.nome)) 
    banco.commit()

def deletar_post(usuario):
    limpaTela()
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    cursor.execute("DELETE FROM posts WHERE usuario = ?",(usuario.nome,))
    banco.commit()

def comentar_post():
    qual_post = input()
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    print("Função a ser implementada")

#cria_tabela_forum()
#novo_post()
#deletar_post()
#ver_posts()
#editar_post()

def main_forum_menu(usuario):
    cria_tabela_forum()
    bem_vindo(usuario)    
    repeat = True 
    while repeat == True:
        menu_inicial_forum()
        opcao = input()
        if opcao == "1":
            limpaTela()
            ver_posts()
        elif opcao == "2":
            novo_post(usuario)
        elif opcao == "3":
            limpaTela()
            print("Ainda será implementado")       
        elif opcao == "4":
            limpaTela()
            editar_post(usuario)   
        elif opcao == "5":
            repeat = False 
            limpaTela()
        else:
            limpaTela()
            print("Opção inválida.")
            sleep(1)