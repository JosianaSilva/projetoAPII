from time import sleep
import os
import sqlite3
from Menus import menu_inicial
from Usuario import Usuario


def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def bem_vindo():
    limpaTela()
    print(f"Seja bem-vindo(a) ao fórum, #usuario!") #temporário, será acossiado a um usuário criado
    sleep(2)
    limpaTela()

def deseja_continuar(x): ##será implementado
    print('Você está indo acessar ' '\033[1m' + x + '\033[0m'+"."' Deseja continuar?')
    desejo = input("s/n")

def menu_inicial_forum():
    print("""Fórum code.Academy (?)
    1. Mostrar postagens
    2. Fazer uma postagem
    3. Procurar postagem
    4. Sair""")

def cria_tabela_forum():
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
    usuario VARCHAR(20) NOT NULL PRIMARY KEY,
    titulo TEXT NOT NULL,
    texto TEXT NOT NULL
    );
    """)
    banco.commit()
    banco.close()

def novo_post(): #adiciona um post ao banco de dados do fórum
    limpaTela()
    print("Fazer um post:")
    usuario = input("Usuário:") ##temporário, será associado a um usuário cadastrado no db de usuários
    titulo = str(input("Título:"))
    texto = input("Texto da postagem:\n")
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
#    titulo_n = '\033[1m' + titulo 
#    cursor.execute("UPDATE posts SET titulo = ?",(titulo_n,))
    cursor.execute("INSERT INTO posts (usuario, titulo, texto) VALUES (?,?,?)",(usuario,titulo,texto))
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

def editar_post():
    limpaTela()
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    nome_usuario = input()
    novo_titulo = input()
    novo_texto = input()
    cursor.execute("""UPDATE posts SET titulo = ?, texto = ? WHERE usuario = ?"""
    ,(novo_titulo,novo_texto,nome_usuario)) 
    banco.commit()

def deletar_post():
    limpaTela()
    nome_usuario = input()
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    cursor.execute("DELETE FROM posts WHERE usuario = ?",(nome_usuario,))
    banco.commit()

def comentar_post():
    qual_post = input()
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    print("Função a ser implementada")

#cria_tabela_forum()
#novo_p()
#deletar_post()
#ver_posts()
#editar_post()

def main_forum_menu():
    bem_vindo()    
    repeat = True 
    while repeat == True:
        menu_inicial_forum()
        opcao = input()
        if opcao == "1":
            limpaTela()
            ver_posts()
        elif opcao == "2":
            novo_post()
        elif opcao == "3":
            limpaTela()
            print("Ainda será implementado")          
        elif opcao == "4":
            repeat = False 
            limpaTela()
        else:
            limpaTela()
            print("Opção inválida.")
            sleep(1)

main_forum_menu()