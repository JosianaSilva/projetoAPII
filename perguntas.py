import time, sys
#DICIONARIOS CRIADOS PARA ARMAZENAR PERGUNTAS, ALTERNATIVAS E RESPOSTAS.
perguntas1  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Considerando a tarefa de beber um refrigerante em lata,\ndetermine as instruções em uma ordem adequada:",
        "alternativas" : {
            "a" : "1.Abrir a tampa; 2.Pegar a lata; 3.Beber o conteúdo." ,
            "b" : "1.Beber o conteúdo; 2.Pegar a lata; 3.Abrir a tampa." ,
            "c" : "1.Abrir a tampa; 2.Beber o conteúdo; 3.Pegar a lata." ,
            "d" : "1.Pegar a lata; 2.Abrir a tampa; 3.Beber o conteúdo." ,
        },
        "resposta_certa" : "d" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "2º Como podemos definir um Algoritmo?",
        "alternativas" : {
            "a" : "Sequência finita de passos que levam à execução de uma tarefa."  ,
            "b" : "Sequência infinita de passos que levam à execução de uma tarefa.",
            "c" : "Sequência finita de passos que não levam á executa de uma tarefa." ,
            "d" : "Sequência infinita de passos que não levam á executa de uma tarefa." ,
        },
        "resposta_certa" : "a",
    },
}

perguntas2  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º São características da linguagem Python, excerto?",
        "alternativas" : {
            "a" : "Linguagem de alto nível."  ,
            "b" : "Suporta múltiplos paradigmas.",
            "c" : "Linguagem de difícil aprendizagem." ,
            "d" : "Tipagem dinâmica." ,
        },
        "resposta_certa" : "c" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "2º Sobre a linguagem Python, é CORRETO afirmar:",
        "alternativas" : {
            "a" : "Linguagem de baixo nível."  ,
            "b" : "Não suporta múltiplos paradigmas.",
            "c" : "Poucas bibliotecas e recursos." ,
            "d" : "Linguagem orientada a objetos." ,
        },
        "resposta_certa" : "d",
    },
}

perguntas3  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Qual é o formato principal de declarar\ne formatar string no Python 3?",
        "alternativas" : {
            "a" : "Aspas simples e Parênteses."  ,
            "b" : "Aspas simples e Aspas duplas.",
            "c" : "Aspas duplas e Parênteses" ,
            "d" : "Aspas duplas e Hashtags." ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "2º Qual dos seguintes itens possui apenas tipos\nde dados da linguagem Python.",
        "alternativas" : {
            "a" : "Tupla; Inteiro; Real; Booleano." ,
            "b" : "String; Inteiro; Tipografia; Booleano." ,
            "c" : "String; Inteiro; Real; Booleano. " ,
            "d" : "String; Temporal; Real; Booleano." ,
        },
        "resposta_certa" : "c",
    },
}

perguntas4  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Qual dos seguintes itens, é INCORRETO afirmar\nque é uma estrutura de decisão:",
        "alternativas" : {
            "a" : "elif" ,
            "b" : "For",
            "c" : "if" ,
            "d" : "else" ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "2º Analise o código Python a seguir.\nwhile x <= 8:\n    print(x, end=' ')\n    x=x+1\nQual a opção que indica a saída produzida pela execução desse código.",
        "alternativas" : {
            "a" : "1 2 3 4 5 6 7 8"  ,
            "b" : "1234567",
            "c" : "8 7 6 5 4 3 2 1" ,
            "d" : "12345678" ,
        },
        "resposta_certa" : "a",
    },
}

perguntas5  = {
    "Primeira pergunta:\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "break",
            "c" : "return" ,
            "d" : "print" ,
        },
        "resposta_certa" : "c" ,
    },
    "Segunda pergunta:\n" : {
        "pergunta" : "2º Considere o código Python a seguir.\na = -4\nb = 0\nc = 2\ndef F(a, b, c):\n    for k in range(a,b):\n        print(k ** c)\nDado que uma execução da função F exibiu os números?",
        "alternativas" : {
            "a" : "16, 9, 4, 1, 0, 1,"  ,
            "b" : "1, 16, 4, 9,",
            "c" : "-4, 0, 2," ,
            "d" : "16, 9, 4, 1," ,
        },
        "resposta_certa" : "d",
    },
}

perguntas6  = {
    "Primeira pergunta:\n" : {
        "pergunta" : "1º Analise o código Python a seguir.\nx = [5,9,8,2,1]\nprint(x[:3])\nQual a opção que indica a saída produzida pela execução desse código.",
        "alternativas" : {
            "a" : "[8,2,1]"  ,
            "b" : "[5,9,8]",
            "c" : "2" ,
            "d" : "[5,9,8,2,1]" ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n" : {
        "pergunta" : "2º Considere o código Python a seguir.\nL=[1, 2, 3, 4]\nL.append(2-12)\nprint(L)\nQual a opção que indica a saída produzida pela execução desse código.",
        "alternativas" : {
            "a" : "[1, 2, 3, 4, -10]"  ,
            "b" : "[1, 2, 3, 4, 12]",
            "c" : "[1, 2, 3, 4, 10]" ,
            "d" : "[1, 2, 3, 4, 2, 12]" ,
        },
        "resposta_certa" : "a",
    },
}

perguntas7  = {
    "Primeira pergunta:\n" : {
        "pergunta" : "Analise a matriz em Python a seguir.\nm = [[1,3,4],[5,6,9]]\nIndique o valor do índice m[1][2]:",
        "alternativas" : {
            "a" : "3" ,
            "b" : "5" ,
            "c" : "4" ,
            "d" : "9" ,
        },
        "resposta_certa" : "d" ,
    },
    "Segunda pergunta:\n" : {
        "pergunta" : "2º Analise o código Python a seguir.\ndef matriz(m):\n    e = 0\n    for l in m:\n        for c in l:\n        e += 1\n    print(elements)\nEssa função ao ser executada, qual seu propósito?",
        "alternativas" : {
            "a" : "Somar todos elementos da matriz m.",
            "b" : "Conta quantos elementos a matriz m possui.",
            "c" : "Fará a soma da diagonal da matriz m." ,
            "d" : "Imprime todos elementos da matriz m." ,
        },
        "resposta_certa" : "b",
    },
}

perguntas8  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Considere a existência de um programa Python, orientado a objetos,\nformado por N classes. Durante sua execução, se não houver problema\nde falta de memória, qual é o número máximo de objetos que podem\nexistir ao mesmo tempo?",
        "alternativas" : {
            "a" : "Exatamente N objetos."  ,
            "b" : "No mínimo N objetos.",
            "c" : "Não há limite para a quantidade de objetos." ,
            "d" : "No máximo N objetos." ,
        },
        "resposta_certa" : "c" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "2º Quando se diz que uma classe “Pessoa” estende a classe “Humano”,\nem Programação Orientada a Objetos,estamos afirmando o mesmo que:",
        "alternativas" : {
            "a" : 'a classe “Humano” é derivada de “Pessoa”.'  ,
            "b" : 'a classe “Humano” é subclasse de “Pessoa”.' ,
            "c" : 'as classes são ditas como “irmãs".' ,
            "d" : 'a classe “Pessoa” deriva da classe “Humano”.' ,
        },
        "resposta_certa" : "d",
    },
}

certas = 0


def prosseguir(certas):         #Recebe certas como pârametro, certas é o contador de respostas.
    quantidade = 2              #Quantidade de perguntas em cada dicionário. 
    porcentagem_acerto = certas / quantidade * 100  #Calcúlo para afim de saber a porcentagem de acertos do usuário.
    print ( f" Você acertou { certas } respostas.\n",f"Sua porcentagem de acerto foi { porcentagem_acerto }%") #Mostra esses números
    if porcentagem_acerto == 100:       #Caso o usuário responda todas certas.
        frase = ("""\033[92m\n=======================\n|  CAPÍTULO CONCLUÍDO |\n=======================\033[0m\n""")
    else:                               #Caso o usuário não acerte todas as perguntas.
        frase = ("\033[91m\n ===========================\n| DESEMPENHO INSATISFATORIO |\n ===========================\033[0m\n")
    for i in list(frase):
        print(i, end="")                #Animação para as condicionais acima.
        sys.stdout.flush()
        time.sleep(0.05)

#Função para exibição das perguntas armazenadas no dicionario.
def pergunta_iLogica(perguntas1, certas):   #Recebe perguntas1(primeiro dicionario) e certas como parâmetro.
    print("\033[93mPERGUNTAS SOBRE LÓGICA DE PROGRAMAÇÃO\033[0m\n")
    for pergunta, dados_pergunta in perguntas1.items():     #For utilizado para acessar a chave da pergunta e resposta.
        print(f"{pergunta}{dados_pergunta['pergunta']}")
        for resposta, dados_resposta in dados_pergunta["alternativas"].items(): #For utilizado para acessar as alternativas.
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("\nSua resposta: ")                #input para o usuário responda as perguntas.
        if resposta_usuario == dados_pergunta["resposta_certa"]:    #Condicional para fim de comparação com a resposta do usuário e a certa.
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")   #Caso o usuário responda certa.
            certas += 1   #Conta as respostas certas.
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")    #Caso o usuário responda errado.
    prosseguir(certas)  #chama a função acima.

#Função para exibição das perguntas armazenadas no dicionario.
def pergunta_iPython(perguntas2, certas):   #Recebe perguntas2(segundo dicionario) e certas como parâmetro.
    print("\033[93mPERGUNTAS SOBRE INTRODUÇÃO Á LINGUAGEM PYTHON\033[0m\n")
    for pergunta, dados_pergunta in perguntas2.items():     
        print(f"{pergunta}{dados_pergunta['pergunta']}")                            #Comportamento igual á anterior
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():    
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("\nSua resposta: ")        
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)

#Função para exibição das perguntas armazenadas no dicionario.
def pergunta_eBasica(perguntas3, certas):    #Recebe perguntas3(terceiro dicionario) e certas como parâmetro.
    print("\033[93mPERGUNTAS SOBRE ESTRUTURA BÁSICA, VARIÁVEIS E TIPO DE DADOS\033[0m\n")
    for pergunta, dados_pergunta in perguntas3.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")                            #Comportamento igual á anterior
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("\nSua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")   
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)

#Função para exibição das perguntas armazenadas no dicionario.
def pergunta_eLogica(perguntas4, certas):   #Recebe perguntas4(quarto dicionario) e certas como parâmetro.
    print("\033[93mPERGUNTAS SOBRE ESTRUTURAS LÓGICAS\033[0m\n")
    for pergunta, dados_pergunta in perguntas4.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")                            #Comportamento igual á anterior
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("\nSua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)

#Função para exibição das perguntas armazenadas no dicionario.
def pergunta_funcoes(perguntas5, certas):   #Recebe perguntas5(quinto dicionario) e certas como parâmetro.
    print("\033[93mPERGUNTAS SOBRE FUNÇÕES\033[0m")
    for pergunta, dados_pergunta in perguntas5.items():     
        print(f"{pergunta}{dados_pergunta['pergunta']}")                            #Comportamento igual á anterior
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():     
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("\nSua resposta: ")        
        if resposta_usuario == dados_pergunta["resposta_certa"]: 
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n") #I
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)

#Função para exibição das perguntas armazenadas no dicionario.
def pergunta_listas(perguntas6, certas):    #Recebe perguntas6(sexto dicionario) e certas como parâmetro.
    print("\033[93mPERGUNTAS SOBRE LISTAS\033[0m")
    for pergunta, dados_pergunta in perguntas6.items():     
        print(f"{pergunta}{dados_pergunta['pergunta']}")                            #Comportamento igual á anterior
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():    
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("\nSua resposta: ")        
        if resposta_usuario == dados_pergunta["resposta_certa"]: 
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)

#Função para exibição das perguntas armazenadas no dicionario.
def pergunta_matriz(perguntas7, certas):    #Recebe perguntas7(sétimo dicionario) e certas como parâmetro.
    print("\033[93mPERGUNTAS SOBRE MATRIZ\033[0m")
    for pergunta, dados_pergunta in perguntas7.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")                            #Comportamento igual á anterior
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("\nSua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)

#Função para exibição das perguntas armazenadas no dicionario.
def pergunta_POO(perguntas8, certas):   #Recebe perguntas8(oitavo dicionario) e certas como parâmetro.
    print("\033[93mPERGUNTAS SOBRE POO\033[0m\n")
    for pergunta, dados_pergunta in perguntas8.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")                            #Comportamento igual á anterior
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("\nSua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)