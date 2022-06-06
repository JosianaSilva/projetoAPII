import os
from time import sleep

def limpaTela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Interrompe o programa e chama o método executaWiki assim q o usuário der Enter
def continua(usuario):
    escolha = input("Clique Enter para voltar")
    executaWiki(usuario)
    # escolha = "n"
    # while(escolha!="s"):
    #     escolha = input("Deseja voltar? (s/n) ")

def MenuWiki():
    menu = """
\tWiki - code.Academy\n 
1. Ver termos
2. Procurar termo
3. Voltar
    """ 
    print(menu)

termos = []

class Termo:
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
        for e in self.exemplos:
            print(e)
        print(2*linhaTabela)
    
    def adicionarExemplo(self, ex):
        self.exemplos.append(ex)

def adicionarTermo(termo):
    termos.append(termo)

def verTermos():
    for t in termos:
        t.mostrarTermo()
        print("")

def procurarTermo(palavraChave):
    resultado = "Resultado da busca: "
    for t in termos:
        if(t.nome == palavraChave):
            print(resultado)
            t.mostrarTermo()
            return True
        else:
            resultado = palavraChave + " não encontrado"
    print(resultado)
    return False

        
    if(procurarTermo(palavraChave)!=True):
        resultado = palavraChave + " não encontrado"
        print(resultado)

#Instanciando alguns termos de teste: 
termo1 = Termo("append","É uma função de listas usada para adicionar um item à lista", "lista.append(novo item)" )
adicionarTermo(termo1)
termo2 = Termo("for","estrutura de repetição que executa uma quantidade predefinida de iterações por meio de uma variável de controle","for i in range(0,10):\n\t\tprint(i)")
adicionarTermo(termo2)
exemplo = """
for item in lista:
    print(item)
"""
termo2.adicionarExemplo(exemplo)

def executaWiki(usuario):
    limpaTela()
    print("Olá, ",usuario.nome,"!")
    MenuWiki() #Mostra as opções
    opW2 = input()
    if(opW2=="1"): #Ver todos os termos
        limpaTela()
        verTermos()
        continua(usuario) #interrompe o programa e chama o método executaWiki assim q o usuário der Enter
    elif(opW2=="2"): #Procurar um termo
        limpaTela()
        palavra = input("Buscar por: ")
        procurarTermo(palavra)
        continua(usuario)
    elif(opW2 == "3"):
        print("Encerrando wiki..")
        sleep(3)
    else:
        print("Opção inválida")
        sleep(3)
        executaWiki(usuario)