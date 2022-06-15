from turtle import title
from functions import *
from Menus import menu_inicial
from CadastroUsuarios import *
from Usuario import *

def texto_menu_forum(): # A parte de texto dos menus.
    formataTitulo(" Fórum code.Academy ")
    print("""
    1. Mostrar postagens
    2. Fazer uma postagem
    3. Procurar postagem
    4. Editar postagem
    5. Deletar postagem
    6. Responder post
    7. Ver comentários
    8. Sair""")

def cria_tabela_forum(): #Cria a tabela da postagens e comentáruios
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS posts (
    id_post INTEGER PRIMARY KEY,
    usuario TEXT NOT NULL,
    titulo TEXT NOT NULL,
    texto TEXT NOT NULL
    );
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS respostas (
    usuario_resposta TEXT NOT NULL,
    id_resposta INTEGER NOT NULL,
    resposta TEXT NOT NULL
    );
    """)
    banco.commit()
    banco.close()

def ver_posts():
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    cursor.execute("SELECT id_post, usuario, titulo, texto FROM posts;")
    try:
        for postagens in cursor.fetchall():
                id_do_post = postagens[0]
                author = postagens[1]
                titulo =  postagens[2]
                texto = postagens[3]
                postAtual = f"""
    [italic cyan]Autor: {author}[/]
    [bold cyan]Título: {titulo}[/]
    [#008080]
    {texto} 
                [/]"""
                print(Panel.fit(postAtual, title = "ID do post:"+str(id_do_post), subtitle_align="center", border_style="blue"))            
    except :
        print("Não há posts ainda!")
    banco.close()

def ver_respostas(): 
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    qual_id = input("Digite o ID do post que você deseja ver os comentários:\n")        
    for comentarios in cursor.execute("SELECT * FROM respostas WHERE id_resposta = ?",(qual_id)):
        author = comentarios[0]
        comentario = comentarios[2]
        coment_atual = f"""
    [bold italic cyan]Autor: {author}[/]
    [#008080]Resposta:\n{comentario}[/]
        """
        print(Panel.fit(coment_atual, title = "Comentário:", subtitle_align="center", border_style="blue"))
    banco.close()


def novo_post(usuario): #Adiciona um post ao banco de dados.
    print("Fazer um post:")
    titulo = (input("Título:\n"))
    texto = input("Texto:\n")
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    cursor.execute("INSERT OR IGNORE INTO posts (usuario, titulo, texto) VALUES (?,?,?)",(usuario.nome,titulo,texto))
    print("Postado!")               
    banco.commit()
    banco.close()

def responder_post(usuario): #Faz uma resposta em um post.
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    qual_id = int(input("Digite o ID do post que você irá responder:\n"))
    resposta = input("Digite sua resposta:\n")
    cursor.execute("INSERT INTO respostas VALUES(?,?,?);",(usuario.nome, qual_id, resposta))
    banco.commit()
    print("Resposta postada!")
    banco.close()    

def procurar_postagem(): #procura uma postagem de acordo com palavra-chave do título.
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    q_titulo = input("Palavra-chave da postagem (título) ")
    cursor.execute("SELECT * FROM posts WHERE titulo LIKE ? COLLATE NOCASE",('%'+ q_titulo +'%',)) 
    for postagens in cursor.fetchall(): # O COLLATE NOCASE a cima é para que a pesquisa não seja "case-sensitive".
            id_do_post = postagens[0] #Ou seja, não importa se o caractere é minúsculo ou maiúsculo
            author = postagens[1]
            titulo =  postagens[2]
            texto = postagens[3]
            postAtual = f"""
    [italic cyan]Autor: {author}[/]
    [bold cyan]Título: {titulo}[/]

    [#008080]{texto}

            """
            print(Panel.fit(postAtual, title = "ID do post:"+str(id_do_post), subtitle_align="center", border_style="blue"))
    banco.close()

def editar_postagem(): #Edita uma postagem com base no ID do post.
    ver_posts()
    banco = sqlite3.connect("forum_database.db")
    with banco:
        cursor = banco.cursor()
        repeat = True
        while repeat == True:
            print("""Digite sua opção:
            1. Editar título  
            2. Editar texto
            3. Editar título e texto
            4. Sair""")
            opcao = input("Digite a opção:\n")
            if opcao == "1":
                limpaTela()
                qual_id = int(input("Digite o ID do post que você irá editar:\n"))
                novo_titulo = input("Digite o novo título:\n")
                cursor.execute("UPDATE posts SET titulo = ? WHERE id_post = ?",(novo_titulo, qual_id))
                print("Alteração feita!")
                banco.commit()
            elif opcao == "2":
                limpaTela()
                qual_id = int(input("Digite o ID do post que você irá editar:\n"))
                novo_texto = input("Digite o novo texto:\n ")
                cursor.execute("UPDATE posts SET texto = ? WHERE id_post = ?",(novo_texto, qual_id))
                banco.commit()
                print("Alteração feita!")                
            elif opcao == "3":
                limpaTela()
                qual_id = int(input("Digite o ID do post que você irá editar:\n"))
                novo_titulo = input("Digite o novo título:\n")
                novo_texto = input("Digite o novo texto:\n ")
                cursor.execute("UPDATE posts SET titulo = ?, texto = ?  WHERE id_post = ?",(novo_titulo,novo_texto, qual_id))
                banco.commit()
                print("Alteração feita!")
            elif opcao == "4":
                limpaTela()
                repeat = False
            else:
                limpaTela()
                print("Opção inválida!")
                sleep(1)


def deletar_post():
    banco = sqlite3.connect("forum_database.db")
    cursor = banco.cursor()
    repeat = True
    while repeat == True:
            ver_posts()
            opcao = input("1. Excluir um post\n2. Voltar para o menu\n")
            if opcao == "1":
                qual_id = input("Qual o ID do post que você deseja deletar? ")
                pergunta = input(f"Você está prestes a deletar o post de ID {qual_id}. Você tem certeza? \n (s/n)\n")
                if pergunta.lower() == "s":
                    cursor.execute("DELETE FROM posts WHERE id_post = ?",(qual_id))        
                    banco.commit()
                    print("Deletado com sucesso")
                    sleep(1)
                elif pergunta.lower() == "n":
                    deletar_post()
                else:
                    limpaTela()
                    print("Opção inválida")
                    sleep(2)
            elif opcao == "2":
                repeat = False
            else:
                limpaTela()
                print("Opção inválida!")


def menu_principal_forum(usuario):
    limpaTela()
    cria_tabela_forum()  
    repeat = True #Condição para manter loop
    while repeat==True:
        limpaTela()
        texto_menu_forum()
        opcao = input("Digite sua opção:\n")
        if opcao=="1":
            limpaTela()
            ver_posts()
        elif opcao=="2":
            novo_post(usuario)
        elif opcao=="3":
            procurar_postagem()
        elif opcao=="4": 
            editar_postagem()
        elif opcao=="5":
            deletar_post()
        elif opcao=="6":
            responder_post(usuario)
        elif opcao=="7":
            ver_respostas()
        elif opcao=="8":
            repeat=False #Quebra o loop e retorna ao menu
        else:
            print("Opção inválida!")
        continua()

