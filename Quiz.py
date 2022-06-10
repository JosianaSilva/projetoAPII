###Tem que importar o comando de limpar a tela e o tempo###
from time import sleep
import os

#função para limpar a tela
def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

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
2. Histórico
3. Voltar(encerra)
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
            showMsg("Não há histórico para mostrar.")           
        elif optMQ=="3":
            repeat=False #quando o usuário pede para sair a condição é alterada e quebra o loop, era pra voltar pro menu principal
            limpaTela()
        else:
            showMsg("Opção inválida!")

#Criação da classe pergunta
class PerguntaQz:
    def __init__(self,id,texto,gabarito):
        self.id = id
        self.texto=texto
        self.gabarito = gabarito.lower()
    
    def askQuestion(self):
        print(self.texto)
        userAnswer = (input())
        if userAnswer==self.gabarito:
            limpaTela()
            print("acertou!")
        else:
            limpaTela()
            print("errou!")

#Pergunta de teste
pergunta1 = PerguntaQz(1,"Quem lidera o projeto?\n[a)Fabrício\nb)Humberto\nc)Izaac\nd)João Victor\ne)Josiana\n","e")

#chamar a função para testar:
# MenuQuizWorks()