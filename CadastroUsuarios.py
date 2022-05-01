from Usuario import *
def cadastroUsuario():
    nome = input("Nome: ")
    email = input("email: ")
    senha = input("Senha: ")
    pontos = 0
    _id = 1+len(users)

    newUser = Usuario(nome,email,senha,pontos,_id)
    users.append(newUser)
    print("Usuário cadastrado com sucesso!")

    return newUser

users = []
