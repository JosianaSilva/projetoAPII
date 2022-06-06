from Usuario import *
# import Usuario as us
import sqlite3
import hashlib
import random

class cadastroUsuario:
    def __init__(self, database):
        self.database = database
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        cursor.execute("""  
        CREATE TABLE IF NOT EXISTS 
            usuario (
                _id integer,
                nome VARCHAR(100) not null,
                email VARCHAR(200),
                pontos NUMERIC,
                senha VARCHAR(32),
                PRIMARY KEY (_id)
                );
        """)
        con.commit()
        con.close()


    def cadastroUsuario(self):
        nome = input("Nome: ")
        email = input("email: ")
        senha = input("Senha: ")
        senha = hashlib.md5(senha.encode()).hexdigest()
        pontos = 0
        # _id = 1+len(usersDicionario.values())
        _id = random.randint(1111,9999)

        newUser = Usuario(nome,email,senha,pontos,_id) 
        #mudar essa parte para o sistema ↑
        usersDicionario[_id] = newUser
        print("Usuário cadastrado com    sucesso!")

        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        consultaInsert = "INSERT INTO usuario (_id,nome, email, senha, pontos) VALUES (?,?,?,?,?);"
        cursor.execute(consultaInsert,(_id,nome,email,senha,pontos))
        con.commit()
        con.close()

        return newUser

    def mostrarUsuariosCadastrados(self):
        con = sqlite3.connect(self.database)
        cursor =  con.cursor()

        consulta = "SELECT nome, email, pontos FROM usuario;"
        cursor.execute(consulta)
        for linha in cursor.fetchall():
            print(f"Nome: {linha[0]}\nE-mail: {linha[1]}\nPontuação:{linha[2]}")
        con.commit()
        con.close()
        # for id in usersDicionario.keys():
        #     usersDicionario[id].mostrarPerfil()

    def procurarUsuario(self, user):

        con = sqlite3.connect(self.database)
        cursor =  con.cursor()

        consulta = "SELECT * from usuario WHERE nome = ?;"
        
        try:
            consulta = cursor.execute(consulta, (user,))
            r = consulta.fetchall()
            if(r[0][1] == user):
                return True
        except:
            # print("Não encontrado")
            return False
        con.commit()
        con.close()

        # for id in usersDicionario.keys():
        #     if(usersDicionario[id].nome == nome):
        #         return True
        #     else:
        #         return False
    
    def getUsuario(self, user):
        con = sqlite3.connect(self.database)
        cursor =  con.cursor()

        consulta = """
        SELECT * from usuario WHERE nome = ?; 
        """
        cursor.execute(consulta, (user,))

        dados = cursor.fetchall()
        #[(1, 'Jo', 's@', 0, '202cb962ac59075b964b07152d234b70')]
        # teste = Usuario("nome", email, senha, pontos, id)
        usuario = Usuario(dados[0][1], dados[0][2],dados[0][4],dados[0][3],dados[0][0])
        return usuario

        con.commit()
        con.close()


    def getSenha(self,user):
        con = sqlite3.connect(self.database)
        cursor =  con.cursor()

        consulta = """
        SELECT * from usuario WHERE nome = ?; 
        """
        cursor.execute(consulta, (user,))
        if(cursor != ""):
            # print(cursor)
            for l in cursor.fetchall():
                senha = l[4]
                return senha
        else:
            print("Não encontrado")
            return False
        con.commit()
        con.close()
usersDicionario = {}
