from perguntas import *
from functions import *

opcao = ""
	
def menuCapitulos1():
    menu = """
\t\033[93m--1º Módulo- code.Academy --\033[0m\n 
1 – Introdução à Lógica de Programação. 
2 – Introdução à Linguagem de Programação Python
3 – Estrutura básica da linguagem Python, declaração de variáveis e tipos de dados.
4 – Estruturas lógicas.
0 – Voltar
    """ 
    print(menu)

def introducaoLogica(opcao):
	with open ("projetoAPII/arquivos/Introdução_Logica.txt","r") as arquivo:
		tx = arquivo.readlines()
		print("".join(map(str, tx[0:24])))  #função join() converter os objetos da lista em strings
		while opcao != "n":
			opcao = input('continuar estudando?\nDigite "s" para sim ou "n" para não: ')
			if opcao == "s":
				print("\x1b[2J", "\n"*1000, "\x1b[1;1H") 
				print("".join(map(str, tx[26:57])))
				break
			elif opcao == "n":
				break
		arquivo.close
	
def introducaoPython():
	with open ("projetoAPII/arquivos/Introdução_Python.txt","r") as arquivo:
		tx = arquivo.readlines()
		print("".join(map(str, tx)))
	arquivo.close

def estruturaBasica(opcao):
	with open ("projetoAPII/arquivos/Estrutura_básica.txt","r") as arquivo:
		tx = arquivo.readlines()
		print("".join(map(str, tx[0:29])))
		while opcao != "n":
			opcao = input('continuar estudando?\nDigite "s" para sim ou "n" para não: ')
			if opcao == "s":
				print("\x1b[2J", "\n"*1000, "\x1b[1;1H")
				print("".join(map(str, tx[29:61])))
				break
		arquivo.close

def estruturaLogicas(opcao):
	with open ("projetoAPII/arquivos/Estruturas_Lógicas.txt","r") as arquivo:
		tx = arquivo.readlines()
		print("".join(map(str, tx[0:29])))
		while opcao != "n":
			opcao = input('continuar estudando?\nDigite "s" para sim ou "n" para não: ')
			if opcao == "s":
				print("\x1b[2J", "\n"*1000, "\x1b[1;1H")
				print("".join(map(str, tx[29:59])))
				break
			elif opcao == "n":
				break
		arquivo.close
					

def execultarModulo1():
	x = ""
	while x != "0":
		menuCapitulos1()
		x = input("Digite uma opção desejada: ")
		limpaTela()
		if x == "1":
			introducaoLogica(opcao)
			continua() #PARA TESTE
			limpaTela()
		elif x == "2":
			introducaoPython()
			continua() #PARA TESTE
			limpaTela()
		elif x == "3":
			estruturaBasica(opcao)
			continua() #PARA TESTE
			limpaTela()
		elif x == "4":
			estruturaLogicas(opcao)
			continua() #PARA TESTE
			limpaTela()
		elif x == "0":
			break
		else:
			print("opção invalida")