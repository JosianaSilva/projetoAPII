from Menus import MenuWiki
from functions import *

    

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

def leTermosDoArquivo():
    with open(r'arquivos\termosWiki.txt', 'r', encoding="utf-8") as arquivo:
        for linha in arquivo:
            trecho = linha.split(";")
            termo = Termo(trecho[0],trecho[1],trecho[2])
            print(termo.nome, ": ",termo.definicao)
            exemplos = str(termo.exemplos[0])
            exemplos = exemplos.format()
            print(exemplos, "\n")
            termo.mostrarTermo()
    arquivo.close()

def procurarTermo(palavraChave):
    resultado = "Resultado da busca: "
    for t in termos:
        if(t.nome == palavraChave):
            print(resultado)
            t.mostrarTermo()
            return True
        
    resultado = palavraChave + " não encontrado"
    print(resultado)
    return False

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
    print("\tOlá, ",usuario.nome,"!")
    MenuWiki() #Mostra as opções
    opW = input()
    if(opW=="1"): #Ver todos os termos
        limpaTela()
        verTermos()
        continua() #interrompe o programa e chama o método executaWiki assim q o usuário der Enter
        executaWiki(usuario)
    elif(opW=="2"): #Procurar um termo
        limpaTela()
        palavra = input("Buscar por: ")
        procurarTermo(palavra)
        continua()
        executaWiki(usuario)

    elif(opW == "3"):
        leTermosDoArquivo()
        print("Encerrando wiki..")
    else:
        print("Opção inválida")
        executaWiki(usuario)