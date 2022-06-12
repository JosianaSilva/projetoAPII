import time, sys
#DICIONARIO CRIADO PARA ARMAZENAR PERGUNTAS, ALTERNATIVAS E RESPOSTAS
perguntas1  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b",
    },
}

perguntas2  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b",
    },
}

perguntas3  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b",
    },
}

perguntas4  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b",
    },
}

perguntas5  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b",
    },
}

perguntas6  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b",
    },
}

perguntas7  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b",
    },
}

perguntas8  = {
    "Primeira pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b" ,
    },
    "Segunda pergunta:\n\n" : {
        "pergunta" : "1º Qual instrução em Python pode ser usar dentro\nde uma função para retonar alguma informação para\nsua ação?",
        "alternativas" : {
            "a" : "pass"  ,
            "b" : "return",
            "c" : "break" ,
            "d" : "print" ,
        },
        "resposta_certa" : "b",
    },
}

certas = 0


def prosseguir(certas):
    quantidade = 2
    porcentagem_acerto = certas / quantidade * 100
    print ( f" Você acertou { certas } respostas.\n",f"Sua porcentagem de acerto foi { porcentagem_acerto }%")
    if porcentagem_acerto == 100:
        frase = ("""\033[92m\n=======================\n|  CAPÍTULO CONCLUÍDO |\n=======================\033[0m\n""")
    else:
        frase = ("\033[91m\n ===========================\n| DESEMPENHO INSATISFATORIO |\n ===========================\033[0m\n")
    for i in list(frase):
        print(i, end="")
        sys.stdout.flush()
        time.sleep(0.05)


def pergunta_iLogica(perguntas1, certas):
    print("\033[93mPERGUNTAS SOBRE LÓGICA DE PROGRAMAÇÃO\033[0m\n")
    for pergunta, dados_pergunta in perguntas1.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("Sua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)


def pergunta_iPython(perguntas2, certas):
    print("\033[93mPERGUNTAS SOBRE INTRODUÇÃO Á LINGUAGEM PYTHON\033[0m\n")
    for pergunta, dados_pergunta in perguntas2.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("Sua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)


def pergunta_eBasica(perguntas3, certas):
    print("\033[93mPERGUNTAS SOBRE ESTRUTURA BÁSICA, VARIÁVEIS E TIPO DE DADOS\033[0m\n")
    certas = 0
    for pergunta, dados_pergunta in perguntas3.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("Sua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)


def pergunta_eLogica(perguntas4, certas):
    print("\033[93mPERGUNTAS SOBRE ESTRUTURAS LÓGICAS\033[0m\n")
    for pergunta, dados_pergunta in perguntas4.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("Sua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)


def pergunta_funcoes(perguntas5, certas):
    print("\033[93mPERGUNTAS SOBRE FUNÇÕES\033[0m\n")
    for pergunta, dados_pergunta in perguntas5.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("Sua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)


def pergunta_listas(perguntas6, certas):
    print("\033[93mPERGUNTAS SOBRE LISTAS\033[0m\n")
    for pergunta, dados_pergunta in perguntas6.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("Sua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)


def pergunta_matriz(perguntas7, certas):
    print("\033[93mPERGUNTAS SOBRE MATRIZ\033[0m\n")
    for pergunta, dados_pergunta in perguntas7.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("Sua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)


def pergunta_POO(perguntas8, certas):
    print("\033[93mPERGUNTAS SOBRE POO\033[0m\n")
    for pergunta, dados_pergunta in perguntas8.items():
        print(f"{pergunta}{dados_pergunta['pergunta']}")
        for resposta, dados_resposta in dados_pergunta["alternativas"].items():
            print(f"{resposta}) {dados_resposta}")
        resposta_usuario = input("Sua resposta: ")
        if resposta_usuario == dados_pergunta["resposta_certa"]:
            print("\033[92mEHHHHHH!!! Você acertou!!!!\033[0m\n")
            certas += 1
        else:
            print("\033[91mIXXIIIII!!! Você ERROU!!!!\033[0m\n")
    prosseguir(certas)