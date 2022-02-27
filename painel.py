from tkinter import *
from tkinter import Tk
import sys
from tkinter import font

#coding: utf-8

fundo = '#fff'
text = '#000'

def Nivel1():
    janela = Tk()
    janela.title('Nível 1')
    
    def Sair():
        sys.exit()
    
    
    title = Label(janela, text="Proibido uso do Agrotóxico Paraquete no Brasil", bg=fundo, fg=text, justify=CENTER, font=("Arial", 24))
    title.place(width=janela.winfo_screenwidth(), rely=0.15)
    
    txt = Label(janela, text='''A Agência de Defesa Agropecuária do Estado do Ceará ADAGRI, vinculada à Secretaria do Desenvolvimento Econômico do Estado do Ceará (SEDET)
    \ncomunica aos produtores rurais que, a partir de 22 de setembro de 2020, ficará proibido a comercialização e o uso do Agrotóxico à Base do Princípio
    \nAtivo Paraquate no Brasil.''', bg=fundo, fg=text, justify=LEFT, font=("Arial", 16))
    txt.place(relx=0.15, rely=0.2)
    
    title2 = Label(janela, text='''COP26: Quase 70% dos territórios indígenas e áreas protegidas
    \nno bioma Amazônia estão ameaçados, diz relatório.''', bg=fundo, fg=text, justify=CENTER, font=("Arial", 24))
    title2.place(width=janela.winfo_screenwidth(), rely=0.35)
    
    txt = Label(janela, text='''Quase 70% dos territórios indígenas e das áreas protegidas em todo o bioma Amazônia estão ameaçados por estradas, mineração, exploração de
    \npetróleo e gás, invasões ilegais, hidrelétricas e desmatamento. O alerta consta no relatório lançado pelo Painel Científico para a Amazônia durante
    \na 26ª Conferência sobre o Clima das Nações Unidas (COP26), em Glasgow, na Escócia.''', bg=fundo, fg=text, justify=LEFT, font=("Arial", 16))
    txt.place(relx=0.15, rely=0.5)

    bt = Button(janela, text="Sair", bd=2, bg='#2f4f4f', highlightbackground='blue', fg='#fff', command=Sair)
    bt.place(relx=0.89, rely=0.02, relwidth=0.10, relheight=0.05)

    wide = "{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight())    

    janela.configure(bg=fundo)
    janela.geometry(wide)
    janela.mainloop()

def Nivel2():
    def Sair():
        sys.exit()
    janela = Tk()
    janela.title('Nível 2')

    title = Label(janela, text="Desertificação atinge 13% do semiárido brasileiro e ameaça conservação da caatinga", bg=fundo, fg=text, justify=CENTER, font=("Arial", 24))
    title.place(width=janela.winfo_screenwidth(), rely=0.15)
    
    txt = Label(janela, text='''Único bioma exclusivamente brasileiro, a caatinga sofre. O famoso chão rachado faz pensar num ambiente onde a terra dá pouco e pede
    \nmuito das pessoas que vivem ali. Mas é a própria ação humana que tem colocado a caatinga em risco. A ponto de, em algumas áreas,
    \na situação chegar a um estágio quase irreversível: a desertificação.''', bg=fundo, fg=text, justify=LEFT, font=("Arial", 16))
    txt.place(relx=0.15, rely=0.2)
    
    title2 = Label(janela, text='''Combate à desertificação na caatinga depende de pesquisa científica e ação de pequenos produtores''', bg=fundo, fg=text, justify=CENTER, font=("Arial", 24))
    title2.place(width=janela.winfo_screenwidth(), rely=0.35)
    
    txt = Label(janela, text='''Quando falamos de "desertificação", é porque os danos causados no solo, pela falta de chuvas e pela ação humana, já são quase irreversíveis.
    \nCombater esse processo não é fácil. Mas algumas iniciativas no Nordeste do Brasil tentam reverter os impactos da desertificação.
    \nEnquanto pesquisadores recorrem à ciência para criar modelos de preservação e recuperação da vegetação nativa, pequenos agricultores
    \nbuscam "conviver bem com o semiárido" e "manter a caatinga em pé".''', bg=fundo, fg=text, justify=LEFT, font=("Arial", 16))
    txt.place(relx=0.15, rely=0.4)

    bt = Button(janela, text="Sair", bd=2, bg='#2f4f4f', highlightbackground='blue', fg=fundo, command=Sair)
    bt.place(relx=0.89, rely=0.02, relwidth=0.10, relheight=0.05)

    wide = "{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight())    

    janela.configure(bg=fundo)
    janela.geometry(wide)
    janela.mainloop()

def Nivel3():
    def Sair():
        sys.exit()
    janela = Tk()
    janela.title('Nível 3')

    title = Label(janela, text="No mês do meio ambiente, licenciamento ambiental provoca debates no Senado", bg=fundo, fg=text, justify=CENTER, font=("Arial", 24))
    title.place(relx=0.17, rely=0.15)
    
    txt = Label(janela, text='''O mês em que se celebra o Dia Mundial do Meio Ambiente (5), senadores assumem a complexa posição de avaliar e definir as regras
    \nque nortearão a Lei Geral do Licenciamento Ambiental (LGLA), por meio do PL 3.729/2004, recém-aprovado na Câmara após 17 anos
    \nde tramitação. Para alcançar o equilíbrio entre proteção ambiental e atividade econômica, base do desenvolvimento sustentável, os
    \nparlamentares vão se deparar com regras gerais que buscam simplificar e agilizar o processo licenciatório, mas que atualmente estão
    \nenvoltas em questionamentos sobre aumento de litigiosidades, vulnerabilidade ambiental e desconfiança internacional.''', bg=fundo, fg=text, justify=LEFT, font=("Arial", 16))
    txt.place(relx=0.15, rely=0.2)
    
    title2 = Label(janela, text='''Assembleia da ONU para o Meio Ambiente termina com chamado urgente para solucionar emergências planetárias''', bg=fundo, fg=text, justify=CENTER, font=("Arial", 24))
    title2.place(width=janela.winfo_screenwidth(), rely=0.45)
    
    txt = Label(janela, text='''Nairóbi, 23 de fevereiro de 2021 - Ministros do meio ambiente e outras lideranças de mais de 150 nações concluíram hoje a reunião online de dois dias da
    \nQuinta Assembleia das Nações Unidas para o Meio Ambiente (UNEA-5). O encontro alertou para o risco de novas pandemias globais - se não mudarmos a
    \nforma como protegemos a natureza. A Assembleia das Nações Unidas para o Meio Ambiente se reúne a cada dois anos para definir as prioridades das
    \npolíticas ambientais globais e desenvolver a legislação ambiental internacional. As decisões e resoluções acordadas pelos Estados-membros também
    \ndefinem o trabalho do Programa das Nações Unidas para o Meio Ambiente (PNUMA). Devido à pandemia, os Estados-membros concordaram com uma
    \nabordagem em duas etapas para a UNEA-5: uma sessão online (22-23 de fevereiro de 2021) e uma reunião presencial planejada para fevereiro de 2022.''', bg=fundo, fg=text, justify=LEFT, font=("Arial", 16))
    txt.place(relx=0.10, rely=0.5)

    bt = Button(janela, text="Sair", bd=2, bg='#2f4f4f', highlightbackground='blue', fg='#fff', command=Sair)
    bt.place(relx=0.89, rely=0.02, relwidth=0.10, relheight=0.05)

    wide = "{0}x{1}+0+0".format(janela.winfo_screenwidth(), janela.winfo_screenheight())    

    janela.configure(bg=fundo)
    janela.geometry(wide)
    janela.mainloop()
    
Nivel3()