# A finalidade desse programa é reunir funções que estavam sendo repetidamente usadas nos demais
# Assim, simplificado a utilização delas em vários arquivos

from time import sleep
import os
from getpass import getpass
import hashlib
import random

def limpaTela():
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

def hash_(string):
    return hashlib.md5(string.encode()).hexdigest() 

# Interrompe o programa e continua a execução assim que o usuário "der" Enter
def continua():
    input("Clique Enter para voltar")
