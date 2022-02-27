#IMPORTAÇÕES DE LIBS
from tkinter import *
from tkinter import messagebox
from tkinter import font
import mysql.connector
import sys

#FUNÇÕES CRIADAS
import painel
import webcam
from webcam import nome, rosto

#FUNÇÃO LOGIN
def Ok():
    global usuario
    usuario = str(user.get())
    senha = password.get()

    #CONECTA COM O BANCO DE DADOS
    conn = mysql.connector.connect(user="root", password="1132", host="localhost", database="APS")
    cursor = conn.cursor()

    #CONSULTA NO BANCO DE DADOS
    sql = "SELECT * FROM `usuarios` WHERE usuario = '"+ usuario +"' AND senha = '"+ senha +"'"
    cursor.execute(sql)
    row = cursor.fetchall()

    #VERIFICA SE O USUARIO EXISTE
    if row:
        messagebox.showinfo('Acesso', 'Acesso Liberado\n Aperte a tecla "Q" para sair do reconhecimento')
        #VERIFICA O NIVEL DE ACESSO DO USUARIO
        level = "SELECT nivel FROM usuarios WHERE usuario = '"+ usuario +"' AND senha = '"+ senha +"'"

        cursor.execute(level)
        lvl = cursor.fetchone()
        if lvl[0] == 1:
            print("")
            webcam.rosto()
            testnome = webcam.rosto()
            testsenha = "SELECT nome FROM usuarios WHERE nome = '" + testnome + "'"
            cursor.execute(testsenha)
            testsenha2 = cursor.fetchone()
            if senha == testsenha2[0]:
                painel.Nivel1()
            else:
                sys.exit()
        elif lvl[0] == 2:
            webcam.rosto()
            testnome = webcam.rosto()
            testsenha = "SELECT nome FROM usuarios WHERE nome = '" + testnome + "'"
            cursor.execute(testsenha)
            testsenha2 = cursor.fetchone()
            if senha == testsenha2[0]:
                painel.Nivel2()
            else:
                sys.exit()
        elif lvl[0] == 3:
            webcam.rosto()
            testnome = webcam.rosto()
            testsenha = "SELECT senha FROM usuarios WHERE nome = '"+ testnome +"'"
            cursor.execute(testsenha)
            testsenha2 = cursor.fetchone()
            if senha== testsenha2[0]:
                painel.Nivel3()
    else:
        messagebox.showerror('Erro', 'Acesso Negado, Usuário ou senha estão incorretos')

janela = Tk()
janela.title('Meio Ambiente - Acesso')
global user
global password

fundo = '#50fa7b'
txtColor = '#000'

txt = Label(janela, text="MINISTÉRIO DO MEIO AMBIENTE", font=('Arial', 18), bg=fundo, fg=txtColor)
txt.place(relx=0.2, rely=0.08)

userLabel = Label(janela, text="Usuário:", font=('Arial', 16), bg=fundo, fg=txtColor)
userLabel.place(relx=0.43, rely=0.2)

#INPUT USUARIO
user = Entry(janela, bd=0, bg='#fff', highlightbackground="#fff", width=25, fg=txtColor)
user.place(relx=0.25, rely=0.27)

passLabel = Label(janela, text="Senha:", font=('Arial', 16), bg=fundo, fg=txtColor)
passLabel.place(relx=0.44, rely=0.35)

#INPUT SENHA
password = Entry(janela, bd=0, show='*', bg='#fff', highlightbackground="#fff", width=25, fg=txtColor)
password.place(relx=0.25, rely=0.42)

#BUTTON LOGIN
entrar = Button(janela, text="Entrar", fg='#000' ,bd=0, font=('', 16), command=Ok)
entrar.place(relx=0.37, rely=0.5, width=120, height=40)

#DIMENSOES
width = 500
height = 500

W_screen = janela.winfo_screenwidth()
H_screen = janela.winfo_screenheight()

posx = W_screen/2 - width/2
posy = H_screen/2 - height/2

janela.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
janela.resizable(width=0, height=0)
janela.configure(bg=fundo)
janela.mainloop()