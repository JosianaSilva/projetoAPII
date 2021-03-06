from Menus import MenuWiki
from functions import *

    
# Esta lista é destinada aos objetos Termo
termos = []
# A lista a seguir contém o nome dos termos já salvos e é usada para ler os arquivos respectivos a cada termo
termosSalvos = ["append","for","funcao","while"]

class Termo:
    def __init__(self, nome, definicao,exemplo):
        self.exemplos = []
        self.nome = nome
        self.definicao = definicao
        self.exemplos.append(exemplo)
     
    def mostrarTermo(self):
        corpoTermo = self.nome + ": "+ self.definicao +"\nExemplo(s):\n\t"   
        console.rule("« "+self.nome+" »", style=" 	#7FFFD4")
        print(corpoTermo)
        for exemplo in self.exemplos:
            for linha in exemplo:
                console.print(linha, style=" 	#008080") 
    
    def formatoTermo(self):
        corpoTermo = self.nome + ": "+ self.definicao +"\nExemplo(s):\n\t" 
        texto  = ""
        texto = corpoTermo
        for exemplo in self.exemplos:
            for linha in exemplo:
                texto += linha 
        return texto

def adicionarTermo(termo):
    termos.append(termo)

def verTermos(pagina):
    for i in range(pagina):
        termos[i].mostrarTermo()
    resposta = input("\tAnterior (1)| Voltar (x) | Próximo (2)\n").lower()
    if(resposta=="1" and pagina!=2):
        limpaTela()
        verTermos(pagina-2)
    elif(resposta=="2" and pagina!=len(termos)):
        limpaTela()
        verTermos(pagina+2)
    elif(resposta == "x"):
        print("Saindo..")
    else:
        msgErro("Opção inválida!")
        verTermos(pagina)
        

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
    with console.status("[blue]Procurando...[/]") as pesquisa:
        limpaTela_(3)
        resultado = "\nResultado da busca: "
        for t in termos:
            if(t.nome == palavraChave):
                console.print(resultado, style="bold underline")
                t.mostrarTermo()
                return True    
        resultado = palavraChave + " não encontrado!"
        console.print(resultado, style="bold underline")
        return False

def executaWiki(usuario):
    limpaTela()
    leArquivosdeTermos()
    MenuWiki() #Mostra as opções
    opW = input()
    if(opW=="1"): #Ver todos os termos
        limpaTela()
        verTermos(2)
        continua() #interrompe o programa e chama o método executaWiki assim q o usuário der Enter
        executaWiki(usuario)
    elif(opW=="2"): #Procurar um termo
        limpaTela()
        palavra = input("Buscar por: ").lower()
        procurarTermo(palavra)
        continua()
        executaWiki(usuario)
    elif(opW == "3"):
        print("Encerrando wiki..")
    else:
        msgErro("Opção inválida")
        executaWiki(usuario)