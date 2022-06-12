from perguntas import *
from functions import *

opcao = ""
        

def menuCapitulos1():
    menu = """
\t--1º Módulo- code.Academy --\n 
1 – Introdução à Lógica de Programação. 
2 – Introdução à Linguagem de Programação Python
3 – Estrutura básica da linguagem Python, declaração de variáveis e tipos de dados.
4 – Estruturas lógicas.
0 – Voltar
    """ 
    print(menu)


def introducaoLogica(opcao):
	def abrirArquivo(caminho, opcao):
		with open (caminho,"r", encoding="utf-8") as arquivo:
			tx = arquivo.readlines()
			print("".join(map(str, tx[0:24])))
			while opcao != "n":
				opcao = input("\033[93mCONTINUAR ESTUDANDO? (s/n): \033[0m")
				if opcao == "s":
					limpaTela() 
					print("".join(map(str, tx[26:57])))
					break
			while opcao != "n":
				opcao = input("VAMOS TESTAR SEU CONHECIMENTO? (s/n): ")
				if opcao == "s":
					limpaTela() 
					pergunta_iLogica(perguntas1, certas)
					break
			arquivo.close
	try:
		abrirArquivo("arquivos/ModArquivos/Introdução_Logica.txt", opcao)
	except:
		abrirArquivo(r"arquivos\\ModArquivos\\Introdução_Logica.txt", opcao)


def introducaoPython(opcao):
	def abrirArquivo(caminho, opcao):
		with open (caminho,"r", encoding="utf-8") as arquivo:
			tx = arquivo.readlines()
			print("".join(map(str, tx)))
			while opcao != "n":
				opcao = input("VAMOS TESTAR SEU CONHECIMENTO? (s/n): ")
				if opcao == "s":
					limpaTela()
					pergunta_iPython(perguntas2, certas)
					break
			arquivo.close
	try:
		abrirArquivo("arquivos/ModArquivos/Introdução_Python.txt", opcao)
	except:
		abrirArquivo(r"arquivos\\ModArquivos\\Introdução_Python.txt", opcao)

def estruturaBasica(opcao):
	def abrirArquivo(caminho, opcao):
		with open (caminho,"r", encoding="utf-8") as arquivo:
			tx = arquivo.readlines()
			print("".join(map(str, tx[0:29])))
			while opcao != "n":
				opcao = input("CONTINUAR ESTUDANDO? (s/n): ")
				if opcao == "s":
					limpaTela()
					print("".join(map(str, tx[29:61])))
					break
			while opcao != "n":
				opcao = input("VAMOS TESTAR SEU CONHECIMENTO? (s/n): ") 
				if opcao == "s":
					limpaTela() 
					pergunta_eBasica(perguntas3, certas)
					break
			arquivo.close
	try:
		abrirArquivo("arquivos/ModArquivos/Estrutura_básica.txt", opcao)
	except:
		abrirArquivo(r"arquivos\\ModArquivos\\Introdução_Python.txt", opcao)


def estruturaLogicas(opcao):
	def abrirArquivo(caminho, opcao):
		with open (caminho,"r", encoding="utf-8") as arquivo:
			tx = arquivo.readlines()
			print("".join(map(str, tx[0:29])))
			while opcao != "n":
				opcao = input("CONTINUAR ESTUDANDO? (s/n): ")
				if opcao == "s":
					limpaTela()
					print("".join(map(str, tx[29:64])))
					break
			while opcao != "n":
				opcao = input("VAMOS TESTAR SEU CONHECIMENTO? (s/n): ")
				if opcao == "s":
					limpaTela() 
					pergunta_eLogica(perguntas4, certas)
					break
			arquivo.close
	try:
		abrirArquivo("arquivos/ModArquivos/Estruturas_Lógicas.txt", opcao)
	except:
		abrirArquivo(r"arquivos\\ModArquivos\\Introdução_Python.txt", opcao)					

def executarModulo1():
	x = ""
	while x != "0":
		limpaTela()
		menuCapitulos1()
		x = input("Digite uma opção desejada: ")
		if x == "1":
			limpaTela()
			introducaoLogica(opcao)
		elif x == "2":
			limpaTela()
			introducaoPython(opcao)
		elif x == "3":
			limpaTela()
			estruturaBasica(opcao)
		elif x == "4":
			limpaTela()
			estruturaLogicas(opcao)
		elif x == "0":
			break
		else:
			print("Opção inválida")