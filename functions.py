# A finalidade desse programa é reunir funções que estavam sendo repetidamente usadas nos demais
# Assim, simplificado a utilização delas em vários arquivos

from time import sleep
import os
from getpass import getpass
import hashlib
import random
from rich.console import Console
from rich import print
from rich.panel import Panel

console = Console()

def limpaTela_(s):
    sleep(s)
    os.system('cls' if os.name == 'nt' else 'clear')

def limpaTela():
    print("\n"*1000)
    os.system('cls' if os.name == 'nt' else 'clear')
    

# Faz a formatação do título:
def formataTitulo(titulo):
    console.rule("[bold blue]"+titulo, style="on blue", align="center")

# Interrompe o programa e continua a execução assim que o usuário "der" Enter
def continua():
    input("Clique Enter para voltar")

def msgErro(msg):
    print("",msg)
    sleep(1)
    print("Tente novamente.")
    limpaTela_(1)

# Função responsável por criar o hash da senha para armazená-la no BD de forma mais segura:
def hash_(string):
    return hashlib.md5(string.encode()).hexdigest() 