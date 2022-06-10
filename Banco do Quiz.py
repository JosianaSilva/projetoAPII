from re import I
from select import select
import sqlite3
from Quiz import *
from functions import continua

def iniciar():
    bancoDePerguntas = sqlite3.connect("perguntas.db")
    cursor =  bancoDePerguntas.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS perguntas(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
enunciado text NOT NULL,
a text NOT NULL,
b text NOT NULL,
c text NOT NULL,
d text NOT NULL,
gabarito VARCHAR(1));""")
    bancoDePerguntas.commit()
    bancoDePerguntas.close()

def inserirPergunta():
    id = int(input("ID: "))
    enunciado = input("enunciado: ")
    a =  input()
    b =  input()
    c =  input()
    d =  input() 
    gabarito = input("Gabarito: ")
    bancoDePerguntas = sqlite3.connect("perguntas.db")
    cursor =  bancoDePerguntas.cursor()
    cursor.execute("INSERT INTO perguntas (id, enunciado, a, b, c, d, gabarito) VALUES(?,?,?,?,?,?,?);",(id,enunciado,a,b,c,d,gabarito))
    bancoDePerguntas.commit()
    bancoDePerguntas.close()

def editarPergunta():
    id_a_editar = int(input("Digite o id da pergunta que deseja editar: " ))
    novo_id = int(input("Novo ID: "))
    novo_a =  input()
    novo_b =  input()
    novo_c =  input()
    novo_d =  input() 
    novo_enunciado = input("Novo enunciado: ")
    novo_gabarito = input("Novo gabarito: ")
    con = sqlite3.connect("perguntas.db")
    cursor = con.cursor()
    edicao = "UPDATE perguntas SET id = ?, enunciado = ?, a = ?, b = ?, c = ?, d = ?, gabarito = ? WHERE id = ?"
    cursor.execute(edicao,(novo_id, novo_enunciado, novo_a, novo_b, novo_c, novo_d, novo_gabarito, id_a_editar))
    con.commit()
    con.close()

def listarPerguntas():
    con = sqlite3.connect("perguntas.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM perguntas")
    print("Lista de perguntas:\n")
    for linha in cursor.fetchall():
        print(f"""ID: {linha[0]}
Enunciado: {linha[1]}
A{linha[2]}
B{linha[3]}
C{linha[4]}
D{linha[5]}
Gabarito: {linha[6]}
""")
    print("----- fim da lista -----")
    con.close()

def removerPergunta():
    con = sqlite3.connect("perguntas.db")
    cursor = con.cursor()
    id_apagar = int(input("ID da Pergunta que deseja deletar: "))
    cursor.execute('DELETE FROM perguntas WHERE id = ?',(id_apagar,))
    con.commit()
    con.close()  

def menuAdmQuiz():
    iniciar()
    repeat =  True
    while repeat:
        limpaTela()
        print("""Gerenciamento de perguntas, o que quer fazer?
1 - inserir
2 - editar
3 - listar
4 - remover
5 - sair""")
        opcao=input()
        if opcao == "1":
            limpaTela()
            inserirPergunta()
            sleep(3)
        elif opcao == "2":
            limpaTela()
            editarPergunta()
            sleep(3)
        elif opcao == "3":
            limpaTela()
            listarPerguntas()
            continua()
        elif opcao == "4":
            limpaTela()
            removerPergunta()
            limpaTela()
        elif opcao == "5":
            limpaTela()
            repeat = False
            sleep(3)
        else:
            limpaTela()
            print("Opção inválida!")
            sleep(3)

menuAdmQuiz()