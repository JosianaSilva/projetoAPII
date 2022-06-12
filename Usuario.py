from collections import deque
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
        historico = deque([])
        historico = deque(pk.load(open(r"arquivos\\HistoricoArquivos\\" + str(self.id) +".score", "rb")))
        return historico

    def mostrarHistorico(self):
        historico = self.getHistorico()
        hisFormatado = ""
        for i in range(len(historico)-1,-1,-1):
            hisFormatado += str(historico[i]) + " "
            # hisFormatado += ponto + " "
        print(f"""Últimas pontuções: {
        {hisFormatado}
        }""")

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
        # if(tam > 10):
        #     while(tam>10):
        #         historicoUsuario.popleft()

        # Na próxima linha será sobrescrito o histórico, adicionando as alterações
        pk.dump(historicoUsuario, open("arquivos\\HistoricoArquivos\\" + str(self.id) +".score", "wb"))
        if(novaPontuacao > self.maiorPontuacao):
            self.maiorPontuacao = novaPontuacao
            atualizaMaiorPontuacao(self.id, self.maiorPontuacao)
    


    def getPontosQuiz(self):
        return self.pontos

    def aumentaPontos(self, pts):
        self.pontos += pts
        atualizaPontos(self.id, self.pontos)


    def mostrarScore(self):
        print(f"{self.nome} : {self.pontos} pontos")

# exemplo de criação de usuário:
# user1 = user("Maria","maria@gmail.com", 1978,0,1)
# user1.mostrarPerfil()