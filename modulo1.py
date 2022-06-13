from perguntas import *
from functions import *  

opcao = ""
        
# Função para exibir o menu:
def menuCapitulos1():
	formataTitulo(" 1º Módulo- code.Academy ")
	menu = """
1 – Introdução à Lógica de Programação. 
2 – Introdução à Linguagem de Programação Python
3 – Estrutura básica da linguagem Python, declaração de variáveis e tipos de dados.
4 – Estruturas lógicas.
0 – Voltar
    """ 
	print(menu)

# Função leitura de "arquivos.txt"
def introducaoLogica(opcao):										#Recebe como parametro á variável opcao.
	def abrirArquivo(caminho, opcao):								#Função usada para escolher o caminho do diretório apartir do seu SO.
		with open (caminho,"r", encoding="utf-8") as arquivo:		#Recebe o dirétorio apartir do objeto "caminho", para leitura.
			tx = arquivo.readlines()								#Adiciona o arquivo em uma lista para manipulação.
			print("".join(map(str, tx[0:30])))						#Imprime na tela o arquivo já manipulado do indíce 0 ao 30.
			while opcao != "n":										
				opcao = input("\033[93mCONTINUAR ESTUDANDO? (s/n): \033[0m")    #Laço criado para que o usuario possa continuar estudando ou não.
				if opcao == "s":												
					limpaTela() 												
					print("".join(map(str, tx[32:64])))							#Imprime na tela o arquivo já manipulado do indíce 32 ao 64.
					break
			while opcao != "n":
				opcao = input("\033[93mVAMOS TESTAR SEU CONHECIMENTO? (s/n): \033[0m") 	 #Laço criado para que o usuário possa responde ao teste de conhecimento ou não.
				if opcao == "s":
					limpaTela() 
					pergunta_iLogica(perguntas1, certas)						#Chama a função que mostra as perguntas referentes ao capítulo.
					break
			arquivo.close #fecha o arquivo
	try:
		abrirArquivo("arquivos/ModArquivos/Introdução_Logica.txt", opcao)    #Diretório Linux\Mac
	except:
		abrirArquivo(r"arquivos\\ModArquivos\\Introdução_Logica.txt", opcao) #Diretório Windows

# Função leitura de "arquivos.txt"
def introducaoPython(opcao):
	def abrirArquivo(caminho, opcao):											#Comportamento igual á anterior
		with open (caminho,"r", encoding="utf-8") as arquivo:
			tx = arquivo.readlines()
			print("".join(map(str, tx)))										#Imprime na tela o arquivo completo já manipulado.
			while opcao != "n":
				opcao = input("\033[93mVAMOS TESTAR SEU CONHECIMENTO? (s/n): \033[0m")
				if opcao == "s":
					limpaTela()
					pergunta_iPython(perguntas2, certas)			
					break
			arquivo.close
	try:
		abrirArquivo("arquivos/ModArquivos/Introdução_Python.txt", opcao)    #Diretório Linux\Mac
	except:
		abrirArquivo(r"arquivos\\ModArquivos\\Introdução_Python.txt", opcao) #Diretório Windows

# Função leitura de "arquivos.txt"
def estruturaBasica(opcao):
	def abrirArquivo(caminho, opcao):
		with open (caminho,"r", encoding="utf-8") as arquivo:					#Comportamento igual á anterior
			tx = arquivo.readlines()
			print("".join(map(str, tx[0:30])))
			while opcao != "n":
				opcao = input("\033[93mCONTINUAR ESTUDANDO? (s/n): \033[0m")
				if opcao == "s":
					limpaTela()
					print("".join(map(str, tx[31:64])))
					break
			while opcao != "n":
				opcao = input("\033[93mVAMOS TESTAR SEU CONHECIMENTO? (s/n): \033[0m") 
				if opcao == "s":
					limpaTela() 
					pergunta_eBasica(perguntas3, certas)
					break
			arquivo.close
	try:
		abrirArquivo("arquivos/ModArquivos/Estrutura_básica.txt", opcao)     #Diretório Linux\Mac
	except:
		abrirArquivo(r"arquivos\\ModArquivos\\Introdução_Python.txt", opcao) #Diretório Windows

# Função leitura de "arquivos.txt"
def estruturaLogicas(opcao):
	def abrirArquivo(caminho, opcao):
		with open (caminho,"r", encoding="utf-8") as arquivo:					#Comportamento igual á anterior
			tx = arquivo.readlines()
			print("".join(map(str, tx[0:33])))
			while opcao != "n":
				opcao = input("\033[93mCONTINUAR ESTUDANDO? (s/n): \033[0m")
				if opcao == "s":
					limpaTela()
					print("".join(map(str, tx[34:67])))
					break
			while opcao != "n":
				opcao = input("\033[93mVAMOS TESTAR SEU CONHECIMENTO? (s/n): \033[0m")
				if opcao == "s":
					limpaTela() 
					pergunta_eLogica(perguntas4, certas)
					break
			arquivo.close
	try:
		abrirArquivo("arquivos/ModArquivos/Estruturas_Lógicas.txt", opcao)    #Diretório Linux\Mac
	except:
		abrirArquivo(r"arquivos\\ModArquivos\\Introdução_Python.txt", opcao)  #Diretório Windows
				


def executarModulo1():
	x = ""
	while x != "0":
		limpaTela()
		menuCapitulos1()  #Mostra as opções do menu
		x = input("Digite uma opção desejada: ")
		if x == "1":
			limpaTela()
			introducaoLogica(opcao)  #executa a função de leitura.
		elif x == "2":
			limpaTela()
			introducaoPython(opcao)  #executa a função de leitura.
		elif x == "3":
			limpaTela()
			estruturaBasica(opcao)   #executa a função de leitura.
		elif x == "4":
			limpaTela()
			estruturaLogicas(opcao)  #executa a função de leitura.
		elif x == "0":
			break                    #Encerra o laço e volta ao passo anterior.
		else:
			print("Opção inválida")