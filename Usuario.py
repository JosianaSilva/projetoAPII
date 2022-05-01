class Usuario():
    def __init__(self, nome, email, senha, pontosQuiz, id):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.pontosQuiz = pontosQuiz
        self.id = id

    def mostrarPerfil(self):
        print("Nome:", self.nome, 
        "\nEmail: ", self.email,
        "\nPontuação:", self.pontosQuiz)

# exemplo de criação de usuário:
# user1 = user("Maria","maria@gmail.com", 1978,0,1)
# user1.mostrarPerfil()