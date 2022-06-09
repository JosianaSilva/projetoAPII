from os import truncate
from Menus import MenuWiki
from functions import *

    
# Esta lista é destinada aos objetos Termo
termos = []
# A lista a seguir contém o nome dos termos já salvos e é usada para ler os arquivos respectivos a cada termo
termosSalvos = ["for", "append","while"]

class Termo:
    def __init__(self, nome, definicao,exemplo):
        self.exemplos = []
        self.nome = nome
        self.definicao = definicao
        self.exemplos.append(exemplo)
     
    def mostrarTermo(self):
        corpoTermo = self.nome + ": "+ self.definicao +"\nExemplo(s):\n\t" 
        divisao = 4*"----------------------------------"
        print(divisao)
        print(corpoTermo)
        for exemplo in self.exemplos:
            for linha in exemplo:
                print(linha)
        print(divisao)
    
    def adicionarExemplo(self, ex):
        self.exemplos.append(ex)

def adicionarTermo(termo):
    termos.append(termo)

def verTermos():
    for t in termos:
        t.mostrarTermo()
        print("")

# O objetivo da seguinte função é buscar os arquivos com as informações e convertê-las em objeto
def leArquivosdeTermos():
    for cada in termosSalvos:
        caminho = 'arquivos\\WikiArquivos\\'+ cada + '.txt'
        with open(caminho, 'r', encoding="utf-8") as arquivo:
            trecho = []
            for linha in arquivo:
                trecho.append(linha)
            termo = Termo(trecho[0],trecho[1],trecho[2:])
            nomeSemEspaço =""
            nomeSemEspaço = termo.nome.split()
            termo.nome = nomeSemEspaço[0] # Apenas para remover espaços vazios
            adicionarTermo(termo)
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

def executaWiki(usuario):
    limpaTela()
    leArquivosdeTermos()
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

        print("Encerrando wiki..")
    else:
        print("Opção inválida")
        executaWiki(usuario)