#TELA INICIAL
from tkinter import *
import login

def Login():
    janela.destroy()
    login.Login()

janela = Tk()
janela.title('Meio Ambiente')

Button(janela, width=12, height=2, text='Entrar', command=Login).place(relx=0.2, rely=0.3)


#CALCULO DE DIMENSOES DA TELA
width = 300
height = 300

W_screen = janela.winfo_screenwidth()
H_screen = janela.winfo_screenheight()

posx = W_screen/2 - width/2
posy = H_screen/2 - height/2

janela.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
janela.mainloop()