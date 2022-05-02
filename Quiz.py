###Tem que importar o comando de limpar a tela e o tempo###
from time import sleep
import os
def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')
###Tem que importar o comando de limpar a tela e o tempo###

### função provisória para exibir mensagem das opções ###
def showMsg(mensagem):
    limpaTela() #limpa a tela
    print(mensagem) #exibe a mensagem
    sleep(2) #espera 2 segundos (não precisa limpar de novo pq o menu já limpa antes de aparecer)

# Função para exibir o menu:
def MenuQuizShow():
    limpaTela()
    print("""------------------------------
menu de quizes - code.Academy:
------------------------------
1. Iniciar Quiz
2. Ver pontuação
3. Histórico
4. Voltar(encerra)
""")

#Função para transitar no menu#
def MenuQuizWorks():  
    repeat = True #coloquei uma condição qualquer para manter um loop
    while repeat==True:
        MenuQuizShow()
        optMQ = input()
        if optMQ=="1":
            showMsg("Instrução: responda com a letra da alternativa.")
            limpaTela()
            pergunta1.askQuestion()
            sleep(3)
        elif optMQ=="2":
            showMsg("Não há pontuações para mostrar.")
        elif optMQ=="3":
            showMsg("Não há histórico para mostrar.")           
        elif optMQ=="4":
            repeat=False #quando o usuário pede para sair a condição é alterada e quebra o loop, era pra voltar pro menu principal
            limpaTela()
        else:
            showMsg("Opção inválida!")



class PerguntaQz:
    def __init__(self,enunciado,alternativas,gabarito):
        self.enunciado=enunciado
        self.alternativas = alternativas
        self.gabarito = gabarito.lower()
    
    def askQuestion(self):
        print(self.enunciado) 
        print(self.alternativas)
        userAnswer = (input())
        if userAnswer==self.gabarito:
            limpaTela()
            print("acertou!")
        else:
            limpaTela()
            print("errou!")

pergunta1 = PerguntaQz("Quem lidera o projeto?", "a)Fabrício\nb)Humberto\nc)Izaac\nd)João Victor\ne)Josiana\n","e")

#chamar a função para testar:
MenuQuizWorks()