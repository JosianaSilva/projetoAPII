# principal utilidade deste programa vai ser organizar as principais funções relacionadas a configurações
# do usuário, enviando-as para o banco de dados

import sqlite3
import hashlib
import os
from time import sleep
from Menus import menuConfig1, menuConfig2

database = "cadastroUsuarios.db"

def continua(usuario):
    input("Clique Enter para voltar")
    executaConfig(usuario)

def limpaTela():
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

def atualizaNome(_id, nomeNovo):
        con = sqlite3.connect(database)
        cursor =  con.cursor()

        consulta = "UPDATE usuario SET nome = ? WHERE _id = ?; "
        cursor.execute(consulta, (nomeNovo,_id))
        
        print("Nome atualizado para: ", nomeNovo)
        con.commit()
        con.close()
def atualizaEmail(_id, emailNovo):
        con = sqlite3.connect(database)
        cursor =  con.cursor()

        consulta = "UPDATE usuario SET email = ? WHERE _id = ?; "
        cursor.execute(consulta, (emailNovo,_id))

        print("Endereço de e-mail atualizado para:", emailNovo)
        con.commit()
        con.close()

def atualizaSenha(_id, senhaNova):
        con = sqlite3.connect(database)
        cursor =  con.cursor()

        consulta = "UPDATE usuario SET senha = ? WHERE _id = ?; "
        cursor.execute(consulta, (senhaNova,_id))


        print("Senha alterada com sucesso. ")
        con.commit()
        con.close()

def executaConfig(usuario):
    limpaTela()
    menuConfig1()
    op = input()
    if(op == "1"):
        usuario.mostrarPerfil()
        continua(usuario)
    elif(op == "2"):
        atualizacoes(usuario)
    elif(op == "3"):
        print("...")
    else:
        print("Opção inválida!")
        executaConfig(usuario)

def atualizacoes(usuario):
    limpaTela()
    menuConfig2()
    op1 = input()
    if(op1 == "1"):
        nome = input("Novo nome: ")
        usuario.setNome(nome)
        atualizaNome(usuario.id, nome)
        atualizacoes(usuario)
    elif(op1 == "2"):
        email = input("Novo endereço de email: ")
        usuario.setEmail(email)
        atualizaEmail(usuario.id, email)
        atualizacoes(usuario)
    elif(op1 == "3"):
        senhaAtual = input("Confirme sua senha atual: ")
        senha = hashlib.md5(senhaAtual.encode()).hexdigest()
        if(senha == usuario.senha):
            usuario.setSenha(senha)
            atualizaSenha(usuario.id, senha)
        else:
            print("Senha incorreta!")
            atualizacoes(usuario)
    elif(op1=="4"):
        print("Voltando...")
        executaConfig(usuario)
    else:
        print("Opção inválida!")
        atualizacoes(usuario)