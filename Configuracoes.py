# principal utilidade deste programa vai ser organizar as principais funções relacionadas a configurações
# do usuário, enviando-as para o banco de dados

import sqlite3
from Menus import menuConfig1, menuConfig2
from functions import *

database = "cadastroUsuarios.db"

def atualizaPontos(_id, pts):
    con = sqlite3.connect(database)
    cursor =  con.cursor()
    consulta = "UPDATE usuario SET pontos = ? WHERE _id = ?; "
    cursor.execute(consulta, (pts, _id))
    con.commit()
    con.close()

def atualizaMaiorPontuacao(_id, pts):
    con = sqlite3.connect(database)
    cursor =  con.cursor()
    consulta = "UPDATE usuario SET maiorPontuacao = ? WHERE _id = ?; "
    cursor.execute(consulta, (pts, _id))
    con.commit()
    con.close()

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

def apagar(usuario):
    id = usuario.id
    con = sqlite3.connect(database)
    cursor =  con.cursor()
    consulta = "DELETE FROM usuario WHERE _id = ?; "
    cursor.execute(consulta, (id,))
    print(usuario.id," Apagado com sucesso. ")
    con.commit()
    con.close()

def executaConfig(usuario):
    limpaTela()
    menuConfig1()
    op = input()
    if(op == "1"):
        usuario.mostrarPerfil()
        continua()
        executaConfig(usuario)
    elif(op == "2"):
        atualizacoes(usuario)
    elif(op == "3"):
        prosseguir = input("Tem certeza que deseja excluir seu perfil? (s/n) \nIsso será irreversível. ")
        if(prosseguir=="s"):
            apagar(usuario)
            continua()
        else:
            executaConfig(usuario)
    elif(op == "4"):
        print("Saindo..")
    else:
        msgErro("Opção inválida!")
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
        senhaAtual = getpass("Confirme sua senha atual: ")
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
        msgErro("Opção inválida!")
        atualizacoes(usuario)