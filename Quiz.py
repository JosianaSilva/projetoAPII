###Tem que importar o comando de limpar a tela e o tempo###
from rich.pretty import Pretty #isso pode ir pro functions.py
from time import sleep
import os
import sqlite3
from functions import *
from Usuario import Usuario


#função para limpar a tela
def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')


### função provisória para exibir mensagem das opções ###
def showMsg(mensagem,color):
    limpaTela() #limpa a tela
    mensagem = "[on "+color+"]"+mensagem+"[/]"
    console.print(mensagem) #exibe a mensagem
    sleep(2) #espera 2 segundos (não precisa limpar de novo pq o menu já limpa antes de aparecer)


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


def mostrarRanking():
    formataTitulo(" Ranking de Pontos acumulados: ")

    listaJogadores = []
    con = sqlite3.connect("cadastroUsuarios.db")
    cursor = con.cursor()
    cursor.execute("SELECT _id, nome, pontos FROM usuario")
    tuplasJogadores = cursor.fetchall()
    con.commit()
    con.close()


    for jogador in tuplasJogadores:
        listaJogadores.append(jogador)
    legenda = "Posição | Ponto    | Usuário"
    print(Panel(legenda,style="violet"))
    for n, i in enumerate(sorted(listaJogadores, key=lambda j: j[2], reverse=True), 1):
        # print(f"   {n}º   |   {i[2]}   -  {i[1]}\n---------------------------")
        rankingString = f"{n}º     |    {i[2]}     |    {i[1]}"
        print(Panel(Pretty(rankingString,justify="left"),style="violet"))
    print()


# Função para exibir o menu:
def MenuQuizShow():
    limpaTela()
    formataTitulo(" menu de quizes - code.Academy ")
    print("""1. Iniciar Quiz
2. Histórico
3. Ranking
4. Desafios bônus
5. Voltar
""")


#Função para transitar no menu#
def MenuQuizWorks(usuario):  
    repeat = True #coloquei uma condição qualquer para manter um loop
    while repeat==True:
        MenuQuizShow()
        optMQ = input()
        if optMQ=="1":
            showMsg("[on red]Instrução:[/] responda com a letra da alternativa.","black")
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
            showMsg("Não há desafios ainda.","red")         
        elif optMQ=="5":
            repeat=False #quando o usuário pede para sair a condição é alterada e quebra o loop, era pra voltar pro menu principal
            limpaTela()
        else:
            showMsg("Opção inválida!", "red")


#chamar a função para testar:
# usuario = Usuario(7410, 'Kite', 'kite@email', 0, 0, '4781ac9273d3335229ca90e8e00a1c71')
# MenuQuizWorks(usuario) 