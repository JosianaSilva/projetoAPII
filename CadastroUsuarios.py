from Usuario import *
import sqlite3
import pickle as pk
from functions import hash_, getpass, random

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
                maiorPontuacao NUMERIC,
                senha VARCHAR(32),
                PRIMARY KEY (_id)
                );
        """) 
        con.commit()
        con.close()

# Função responsável por instanciar um novo usuário e colocar seus dados no BD
    def cadastroUsuario(self):
        nome = input("Nome: ")
        email = input("email: ")
        senha = getpass("Senha: ")
        senha = hash_(senha)
        pontos = 0
        maiorPontuacao = 0
        id = random.randint(1111,9999)
        historico = []

        newUser = Usuario(nome,email,senha,pontos,maiorPontuacao,id) 

        caminho = "arquivos\\HistoricoArquivos\\" + str(newUser.id) +".score"
        pk.dump(historico, open(caminho, "wb"))
        #mudar essa parte para o sistema ↑
        usersDicionario[id] = newUser
    
        con = sqlite3.connect(self.database)
        cursor = con.cursor()
        consultaInsert = "INSERT INTO usuario (_id,nome, email, senha, pontos, maiorPontuacao) VALUES (?,?,?,?,?,?);"
        cursor.execute(consultaInsert,(id,nome,email,senha,pontos,maiorPontuacao))
        con.commit()
        con.close()

        return newUser

    def mostrarUsuariosCadastrados(self):
        con = sqlite3.connect(self.database)
        cursor =  con.cursor()

        consulta = "SELECT nome, email, pontos, _id FROM usuario;"
        cursor.execute(consulta)
        for linha in cursor.fetchall():
            print(f"Nome: {linha[0]} | E-mail: {linha[1]} | Pontuação:{linha[2]} | {linha[3]}")
        con.commit()
        con.close()
        # for id in usersDicionario.keys():
        #     usersDicionario[id].mostrarPerfil()

# Procura no BD o usuário a partir do nome:
    def procurarUsuario(self, username):
        con = sqlite3.connect(self.database)
        cursor =  con.cursor()

        consulta = "SELECT * FROM usuario WHERE nome = ?;"
        
        try:
            consulta = cursor.execute(consulta, (username,))
            objTemp = consulta.fetchall() # objTemp vai armazenar o objeto
            if(objTemp[0][1] == username): # objTemp[0][1] armazena o nome
                return True
        except:
            return False
        con.commit()
        con.close()

        # for id in usersDicionario.keys():
        #     if(usersDicionario[id].nome == nome):
        #         return True
        #     else:
        #         return False
    
# Monta o objeto Usuário a partir do nome e compara com os dados do BD:
    def getUsuario(self, user):
        con = sqlite3.connect(self.database)
        cursor =  con.cursor()

        consulta = " SELECT * FROM usuario WHERE nome = ?; "
        cursor.execute(consulta, (user,))

        dados = cursor.fetchall()
        # instanciando um usuário (nome, email, senha, pontosQuiz, maiorPontuacao, id):
        usuario = Usuario(dados[0][1],dados[0][2], dados[0][5],dados[0][4],dados[0][3],dados[0][0])
        
        con.commit()
        con.close()
        return usuario


# Procura a senha a partir do nome de usuário fornecido:
    def getSenha(self,username):
        con = sqlite3.connect(self.database)
        cursor =  con.cursor()

        consulta = "SELECT * from usuario WHERE nome = ?;"
        cursor.execute(consulta, (username,))
        if(cursor != ""):
            for l in cursor.fetchall():
                senha = l[5]
                return senha
        else:
            print("Não encontrado")
            return False
        con.commit()
        con.close()
usersDicionario = {}