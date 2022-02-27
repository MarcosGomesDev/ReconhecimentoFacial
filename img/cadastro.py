from tkinter import *
from tkinter import messagebox
import mysql.connector
import hashlib
import login

def Ok():
    user = str(usuari.get())
    name = str(nome.get())
    insert = str(senha.get()).encode()
    level = int(nivel.get())
    
    hash = hashlib.md5(insert)
    hashed = hash.hexdigest()

    conn = mysql.connector.connect(user="root", password="", host="localhost", database="aps")
    cursor = conn.cursor()

    try:
        sql = "INSERT INTO `usuarios` (nome, usuario, senha, nivel) VALUES (%s, %s, %s, %s)"
        val = (user, name, hashed, level)
        cursor.execute(sql, val)
        conn.commit()
        messagebox.showinfo('Sucesso', 'Usuário cadastrado com sucesso')
        janela.destroy()
        login.Login()
    except Exception as e:
        print(e)
        conn.rollback()
        conn.close()

janela = Tk()
janela.title('cadastro')
global usuario
global nome
global senha
global nivel

usuari = Entry(janela, bd=0)
usuari.place(relx=0.3, rely=0.17)

nome = Entry(janela, bd=0)
nome.place(relx=0.3, rely=0.32)

senha = Entry(janela, bd=0)
senha.place(relx=0.3, rely=0.47)

nivel = Entry(janela, bd=0)
nivel.place(relx=0.3, rely=0.62)

Button(janela, text='Cadastrar', command=Ok, height=4, width=12).place(relx=0.2, rely=0.8)

janela.geometry('500x500')
janela.mainloop()