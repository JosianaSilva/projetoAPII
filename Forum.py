from turtle import title
from functions import *
from Menus import menu_inicial
from CadastroUsuarios import *
from Usuario import *

database = "forum_database.db"

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

def cria_tabela_forum(): #Cria a tabela das postagens e comentários
    banco = sqlite3.connect(database)
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


def contador_resposta2(): ##função ainda em fase de testes
    banco = sqlite3.connect(database)
    cursor = banco.cursor()
    for y in cursor.execute("SELECT id_resposta, COUNT(resposta) FROM respostas GROUP BY id_resposta"):
        print(f" ID:{y[0]} \n Qtd respostas:{y[1]} ")
    banco.close()
    
#contador_resposta2()

def ver_posts():
    banco = sqlite3.connect(database)
    cursor = banco.cursor()
    cursor.execute("SELECT EXISTS (SELECT id_post FROM posts);")
    if cursor.fetchall()[0][0] != 0:  
        for post in cursor.execute("SELECT * FROM posts"): #id == post[0] #texto == post[3]
            postagem = f"""
[bold]Autor: {post[1]} [/]
Título: {post[2]} 

{post[3]}"""
            print(Panel(postagem, expand = False, title ="[bold cyan]ID do post: " + str(post[0]), border_style="blue"))
    else:
        nao_existe = "[red]Não existe nenhuma postagem ainda!"
        print(Panel(nao_existe, expand = False, border_style="white"))







def ver_respostas(): 
    banco = sqlite3.connect(database)
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
    print("Texto:")
    conteudo = []
    while True: # Cria um loop para o usuário inserir quantos inputs quiser.
        try:
            texto = input("\nPressione Ctrl + Z e aperte Enter para postar!\n")
        except EOFError: # Quando Ctrl Z é pressionado, ele chama o EOFError
            break
        conteudo.append(texto) #O conteúdo digitado vai para a lista "conteúdo"
        conver = "\n".join(map(str,conteudo)) #A lista é convertida em string.
                # ^ Adiciona quebra de linha ao final de cada elemento
    banco = sqlite3.connect(database)
    cursor = banco.cursor()
    cursor.execute("INSERT OR IGNORE INTO posts (usuario, titulo, texto) VALUES (?,?,?)",(usuario.nome,titulo,conver))
    print("Postado!")               
    banco.commit()
    banco.close()
    

def responder_post(usuario): #Adiciona uma resposta a um post caso exista um post com aquele ID
    banco = sqlite3.connect(database)
    cursor = banco.cursor()
    try:
        qual_id = int(input("Digite o ID do post que você irá responder:\n"))
        cursor.execute("SELECT EXISTS (SELECT id_post FROM posts WHERE id_post = ?);", (qual_id,))
        if cursor.fetchall()[0][0] != 0:                
            resposta = input("Digite sua resposta:\n")
            cursor.execute("INSERT INTO respostas VALUES(?,?,?);",(usuario.nome, qual_id, resposta))
            banco.commit()
            print("Resposta postada!")
            banco.close()
        else:
            nao_existe = "[red]Não existe nenhuma postagem com esse ID!"
            print(Panel(nao_existe, expand = False, border_style="white"))
    except ValueError:
        print("O ID deve ser um valor inteiro!")   

def procurar_postagem(): #procura uma postagem de acordo com palavra-chave do título.
    banco = sqlite3.connect(database)
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
    banco = sqlite3.connect(database)
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
    banco = sqlite3.connect(database)
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
    repeat = True 
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
            repeat=False
        else:
            print("Opção inválida!")
        continua()

#menu_principal_forum(Usuario("Tester","aa","123",1,1,123))