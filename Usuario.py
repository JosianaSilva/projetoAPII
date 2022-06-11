from collections import deque
import pickle as pk
from functions import *

# from Configuracoes import atualizaEmail, atualizaNome, atualizaSenha
class Usuario():
    def __init__(self, nome, email, senha, pontosQuiz, maiorPontuacao, id):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.pontosQuiz = pontosQuiz
        self.maiorPontuacao = maiorPontuacao
        self.id = id

    def mostrarPerfil(self):


        perfil = f"""
        ■   [bold]Nome:[/] {self.nome}                     
        ■   [bold]Email:[/] {self.email}                    
        ■   [bold]Pontos:[/] [green]{self.pontosQuiz}[/]              
        ■   [bold]Maior Pontuação:[/] [green]{self.maiorPontuacao}[/] 
        """
        print(Panel.fit(perfil, title="Perfil"))
    
    def mostrarHistorico(self):
        tam = len(self.historicoUsuario)
        print("Histórico de Pontuações - ", self.nome, end=" ")
        for h in range(tam):
            print(self.historicoUsuario[h], end=" ")

    def getHistorico(self):
        historico = deque([])
        historico = pk.load(open("arquivos\\HistoricoArquivos\\" + str(self.id) +".score", "rb"))
        return historico

    def mostrarHistorico(self):
        historico = self.getHistorico()
        hisFormatado = ""
        for ponto in historico:
            hisFormatado += ponto + " "
        print("(",hisFormatado," )")

    def setNome(self, novoNome):
        self.nome = novoNome
    
    def setSenha(self, novaSenha):
        self.senha = novaSenha
    
    def setEmail(self, novoEmail):
        self.email = novoEmail


    def adicionaPontosAoHistorico(self, novo):
        historicoUsuario = self.getHistorico()

        tam = len(historicoUsuario)
        if(tam==10):
            historicoUsuario.popleft()
        historicoUsuario.append(novo)
        if(tam > 10):
            while(tam>10):
                historicoUsuario.popleft()
        # Na próxima linha será sobrescrito o histórico, adicionando as alterações
        pk.dump(open("arquivos\\HistoricoArquivos\\" + str(self.id) +".score", "wb"))
        if(novo > maiorPontuacao):
            maiorPontuacao = novo
    


    def getPontosQuiz(self):
        return self.pontosQuiz

    def aumentaPontos(self, pts):
        self.pontosQuiz += pts
    
    def mostrarScore(self):
        print(f"{self.nome} : {self.pontosQuiz} pontos")

# exemplo de criação de usuário:
# user1 = user("Maria","maria@gmail.com", 1978,0,1)
# user1.mostrarPerfil()