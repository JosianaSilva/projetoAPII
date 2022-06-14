import sqlite3
from functions import * # arquivo de funções utéis
from Usuario import Usuario # dados do usuário


def mensagemColorida(mensagem,cor):
    limpaTela() # limpa a tela
    mensagem = "[on "+cor+"]"+mensagem+"[/]" # formata para colorido
    console.print(mensagem) # exibe a mensagem
    sleep(2) # espera 2 segundos


# exibe o quiz para o usuário responder e somar pontos
def perguntarPerguntas(usuario):
    pontuacao_atual = 0
    con = sqlite3.connect("perguntas.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM perguntas;")
    for linha in cursor.fetchall():
        print(f"""({linha[0]}) {linha[1]}
|A) {linha[2]}
|B) {linha[3]}
|C) {linha[4]}
|D) {linha[5]}
""")
        resposta = input("Qual a resposta? ").lower()
        if resposta == linha[6]:
            print("Acertou!\n")
            pontuacao_atual+=linha[7]
        else:
            print("Errou\n")
    print("pontuação adquirida:",pontuacao_atual)
    usuario.adicionaPontosAoHistorico(pontuacao_atual)
    con.commit()
    con.close()
    

# exibe os jogadores em ordem por pontuação acumulada
def mostrarRanking():
    formataTitulo(" Ranking de Pontos acumulados: ")
    listaJogadores = [] # lista vazia para armazenar
    con = sqlite3.connect("cadastroUsuarios.db")
    cursor = con.cursor()
    cursor.execute("SELECT _id, nome, pontos FROM usuario") # seleciona informaçoes necessárias
    tuplasJogadores = cursor.fetchall() # guarda tudo em tuplas
    con.commit()
    con.close()
    for jogador in tuplasJogadores: # armazena as tuplas numa lista
        listaJogadores.append(jogador)
    legenda = "Posição | Ponto    | Usuário"
    print(Panel(legenda,style="#32556E")) #outra função de texto colorido
    # a seguir: enumerate para percorrer indexando a partir do 1 (1º,2º...)
    #           sorted com reverse true, para ordenar as pontuações em ordem decrescente
    #           função anônima lambda para indicar o elemento para basear a ordenação das tuplas (j[n][2])
    for n, i in enumerate(sorted(listaJogadores, key=lambda j: j[2], reverse=True), 1):
        rankingString = f"{n}º     |    {i[2]}     |    {i[1]}"
        print(Panel(Pretty(rankingString,justify="left"),style="#32556E"))
    print()


# sugere desafios ao usuário, escritas em um arquivo de texto:
def mostrarDesafios():
    formataTitulo(" Desafios Bônus ")
    with(open("arquivos\\desafios.txt", "r",encoding="utf-8")) as leituraArquivo:
        texto = leituraArquivo.read()
    leituraArquivo.close()
    console.print(texto)


# exibe as opções do menu:
def textoMenuQuiz():
    limpaTela()
    formataTitulo(" menu de quizes - code.Academy ")
    print("""1. Iniciar Quiz
2. Histórico
3. Ranking
4. Desafios bônus
5. Voltar
""")


# função principal do quiz
def menuQuiz(usuario):  
    repetir = True # condição de repetição é iniciada como verdadeira
    while repetir: # o menu segue sendo exibido após cada ação até que o usuário opte por sair
        textoMenuQuiz()
        optMQ = input()
        if optMQ=="1":
            mensagemColorida("[on red]Instrução:[/] responda com a letra da alternativa.","black")
            limpaTela()
            perguntarPerguntas(usuario)
            continua()
        elif optMQ=="2":
            limpaTela()
            usuario.mostrarHistorico()
            continua()
        elif optMQ=="3":
            limpaTela()
            mostrarRanking()
            continua()
        elif optMQ=="4": 
            limpaTela()
            mostrarDesafios()
            continua()       
        elif optMQ=="5": # ao escolher sair, o usuário inverte a condição de repetição do menu
            repetir=False 
            limpaTela()
        else: # para qualquer entrada não válida.
            mensagemColorida("Opção inválida!", "red")


# usuario exemplo pra entrar direto no quiz por aqui e função para chamar o menu do quiz:
# usuario = Usuario(7410, 'Kite', 'kite@email', 0, 0, '4781ac9273d3335229ca90e8e00a1c71')
# menuQuiz(usuario) 