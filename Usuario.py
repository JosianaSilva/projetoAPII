from collections import deque
from mailbox import NoSuchMailboxError
import pickle as pk
from Configuracoes import atualizaMaiorPontuacao, atualizaPontos
from functions import *

# from Configuracoes import atualizaEmail, atualizaNome, atualizaSenha
class Usuario():
    def __init__(self, nome, email, senha, pontosQuiz, maiorPontuacao, id):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.pontos = pontosQuiz
        self.maiorPontuacao = maiorPontuacao
        self.id = id

    def mostrarPerfil(self):
        perfil = f"""
        ♦   [bold]Nome:[/] {self.nome}                     
        ♦   [bold]Email:[/] {self.email}                    
        ♦   [bold]Pontos:[/] [green]{self.pontos}[/]              
        ♦   [bold]Maior Pontuação:[/] [green]{self.maiorPontuacao}[/] 
        """
        print(Panel.fit(perfil, title="Perfil"))
    
    def mostrarHistorico(self):
        tam = len(self.historicoUsuario)
        print("Histórico de Pontuações - ", self.nome, end=" ")
        for h in range(tam):
            print(self.historicoUsuario[h], end=" ")

    def getHistorico(self):
        try: 
            lista = pk.load(open("arquivos\\HistoricoArquivos\\" + str(self.id) +".score", "rb"))
        except: # caso não consiga encontrar o arquivo do histórico, ser criado um novo:
            lista = []
            pk.dump(lista, open("arquivos\\HistoricoArquivos\\" + str(self.id) +".score", "wb"))
        historico = deque(lista)
        return historico

    def mostrarHistorico(self):
        historico = self.getHistorico()
        if len(historico)==0:
            console.print("[yellow on black]Histórico vazio.[/]")
        else:
            hisFormatado = "\n"
            for i in range(len(historico)-1,-1,-1):
                hisFormatado += "► obteve "+str(historico[i])+ " pontos.\n"
            titulo = "Ultimas pontuações de "+self.nome+":"
            print(Panel.fit(hisFormatado, title = titulo, style="green", subtitle_align="center", border_style="blue"))
     

    def setNome(self, novoNome):
        self.nome = novoNome
    
    def setSenha(self, novaSenha):
        self.senha = novaSenha
    
    def setEmail(self, novoEmail):
        self.email = novoEmail

    def adicionaPontosAoHistorico(self, novaPontuacao):
        historicoUsuario = self.getHistorico()
        tam = len(historicoUsuario)
        
        if(tam==10):
            historicoUsuario.popleft()
        historicoUsuario.append(novaPontuacao)
        self.aumentaPontos(novaPontuacao)

        # Na próxima linha será sobrescrito o histórico, adicionando as alterações
        pk.dump(historicoUsuario, open("arquivos\\HistoricoArquivos\\" + str(self.id) +".score", "wb"))
        if(novaPontuacao > self.maiorPontuacao):
            self.maiorPontuacao = novaPontuacao
            atualizaMaiorPontuacao(self.id,novaPontuacao)
    
    def getPontosQuiz(self):
        return self.pontos

    def aumentaPontos(self, pts):
        self.pontos += pts
        atualizaPontos(self.id, self.pontos)

    def mostrarScore(self):
        print(f"{self.nome} : {self.pontos} pontos")