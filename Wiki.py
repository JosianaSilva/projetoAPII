import os
from time import sleep

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def escolha():
    escolha = "n"
    while(escolha!="s"):
        escolha = input("Deseja voltar? (s/n) ")

def MenuWiki():
    menu = """
\tWiki - code.Academy\n 
1. Ver termos
2. Procurar termo
3. Voltar
    """ 
    print(menu)

termos = []
class termo():
    def __init__(self, nome, definicao,exemplo):
        self.exemplos = []
        self.nome = nome
        self.definicao = definicao
        self.exemplos.append(exemplo)
     
    def mostrarTermo(self):
        corpoTermo = self.nome + ": "+ self.definicao +"\nExemplo(s):\n\t" 
        linhaTabela = "-------------------------------------------------------"
        print(2*linhaTabela)
        print(corpoTermo)
        for i in self.exemplos:
            print(i)
        print(2*linhaTabela)
    
    def adicionarExemplo(self, ex):
        self.exemplos.append(ex)

def adicionarTermo(termo):
    termos.append(termo)

def verTermos():
    for i in termos:
        print(i.mostrarTermo(),"\n")

def procurarTermo(palavraChave):
    resultado = ""
    for i in termos:
        if(i.nome == palavraChave):
            resultado = i.mostrarTermo()
            break
        else:
            resultado = palavraChave + " não encontrado"
    print(resultado)

#Instanciando alguns termos de teste: 
termo1 = termo("append","É uma função de listas usada para adicionar um item à lista", "lista.append(novo item)" )
adicionarTermo(termo1)
termo2 = termo("for","estrutura de repetição que executa uma quantidade predefinida de iterações por meio de uma variável de controle","for i in range(0,10):\n\t\tprint(i)")
adicionarTermo(termo2)
exemplo = """
for item in lista:
    print(item)
"""
termo2.adicionarExemplo(exemplo)

def executaWiki():
    opW = ""
    while(opW != "3"):
        limpaTela()
        MenuWiki()
        opW2 = input()

        if(opW2=="1"): #Ver todos os termos
            limpaTela()
            verTermos()
            escolha()
            
        elif(opW2=="2"): #Procurar um termo
            limpaTela()
            palavra = ""
            palavra = input("Buscar por: ")
            procurarTermo(palavra)
            escolha()
           
        elif(opW2=="3"): #Sair 
            opW = opW2

        else:
            opW = input()
# executaWiki()