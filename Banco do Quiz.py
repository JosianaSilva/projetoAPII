import sqlite3
from Quiz import *
from functions import *


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
gabarito VARCHAR(1),
valor INTEGER);""")
    bancoDePerguntas.commit()
    bancoDePerguntas.close()


def inserirPergunta():
    id = int(input("ID: "))
    enunciado = input("enunciado: ")
    a =  input("a: ")
    b =  input("b: ")
    c =  input("c: ")
    d =  input("d: ") 
    gabarito = input("Gabarito: ")
    valor = int(input("Valor: "))
    bancoDePerguntas = sqlite3.connect("perguntas.db")
    cursor =  bancoDePerguntas.cursor()
    cursor.execute("INSERT INTO perguntas (id, enunciado, a, b, c, d, gabarito, valor) VALUES(?,?,?,?,?,?,?,?);",(id,enunciado,a,b,c,d,gabarito,valor))
    bancoDePerguntas.commit()
    bancoDePerguntas.close()


def editarPergunta():
    id_a_editar = int(input("Digite o id da pergunta que deseja editar: " ))
    novo_id = int(input("Novo ID: "))
    novo_enunciado = input("Novo enunciado: ")
    novo_a =  input("a: ")
    novo_b =  input("b: ")
    novo_c =  input("c: ")
    novo_d =  input("d: ") 
    novo_gabarito = input("Novo gabarito: ")
    novo_valor = int(input("novo valor: "))
    con = sqlite3.connect("perguntas.db")
    cursor = con.cursor()
    edicao = "UPDATE perguntas SET id = ?, enunciado = ?, a = ?, b = ?, c = ?, d = ?, gabarito = ?, valor = ? WHERE id = ?"
    cursor.execute(edicao,(novo_id, novo_enunciado, novo_a, novo_b, novo_c, novo_d, novo_gabarito, novo_valor, id_a_editar))
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
|A) {linha[2]}
|B) {linha[3]}
|C) {linha[4]}
|D) {linha[5]}
Gabarito: {linha[6]}
Valor: {linha[7]}
""")
    print("----- fim da lista -----")
    con.commit()
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
        elif opcao == "2":
            limpaTela()
            editarPergunta()
        elif opcao == "3":
            limpaTela()
            listarPerguntas()
            continua()
        elif opcao == "4":
            limpaTela()
            removerPergunta()
        elif opcao == "5":
            limpaTela()
            repeat = False
        else:
            limpaTela()
            print("Opção inválida!")


#perguntarPerguntas()
#menuAdmQuiz()