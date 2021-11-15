# Importando as bibliotecas necessárias
import tkinter
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3

# Criando a conexão com o banco de dados "aluno.db"
# Função para criar a tabela "TB_ESCOLA" dentro do banco de dados "aluno.db"
def criar_tabela():
    global conn, cursor
    conn = sqlite3.connect('aluno.db')
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS TB_ESCOLA (
                        id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                        matricula INTEGER NOT NULL,
                        nome TEXT NOT NULL,
                        email TEXT NOT NULL,
                        endereco TEXT NOT NULL,
                        campus TEXT,
                        periodo INTEGER,
                        av1 FLOAT,
                        av2 FLOAT,
                        av3 FLOAT,
                        avd FLOAT,
                        avds FLOAT)''')
    except Exception as e:
        tkMessageBox.showinfo("Atenção: ", "Erro ao criar o banco!", e)
#        print("Erro na criação da tabela: ", e)

# Criando a interface gráfica para inserção dos dados na tabela "TB_ESCOLA"
def JanelaPrincipal():
    #creating window
    janela = Tk()
    janela.geometry("1024x680")
    janela.title("Cadasatro de Alunos")
    global tree
    global SEARCH
    global matricula,nome,email,endereco,campus,periodo,av1,av2,av3,avd,avds
    SEARCH = StringVar()
    matricula = StringVar()
    nome = StringVar()
    email = StringVar()
    endereco = StringVar()
    campus = StringVar()
    periodo = StringVar()
    av1 = StringVar()
    av2 = StringVar()
    av3 = StringVar()
    avd = StringVar()
    avds = StringVar()

# Criação dos Frames de Layout
# Frame de cabeçalho no Topo da janela
    TopViewForm = Frame(janela, width="600", bd=2, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=BOTH, expand=YES)

# Frame a esquerda para inserção dos dados:
    LFrom = Frame(janela, width="350", bd=2, bg="grey")
    LFrom.pack(side=LEFT, fill=BOTH, expand=YES)

# Segundo Frame para pesquisa dos dados
    LeftViewForm = Frame(janela, width="500", bd=2, bg="dark gray")
    LeftViewForm.pack(side=LEFT, fill=BOTH, expand=YES)

# Terceiro Frame para exibir os registros no banco em
    MidViewForm = Frame(janela, width="900", bd=0, bg="white")
    MidViewForm.pack(side=RIGHT, fill=BOTH,  expand=YES)

# Título no topo do Frame da janela
    lbl_text = Label(TopViewForm, text="Gerenciamento de Cadastro de  Alunos", font=('verdana', 18), width=1000,bg="dark grey")
    lbl_text.pack(fill=BOTH)

# Criando o relacionamento dos campos do banco de dados com as caixas de texto na janela principal
    Label(LFrom, text=" Preencha para novo Cadastro ", font=("Arial", 14),bg="grey",fg="white").pack(side=TOP)
    Label(LFrom, text="Matricula  ", font=("Arial", 12),bg="grey",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial",10,"bold"),textvariable=matricula).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Nome ", font=("Arial", 12),bg="grey",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=nome).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Email ", font=("Arial", 12),bg="grey",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=email).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Endereço ", font=("Arial", 12),bg="grey",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=endereco).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Campus ", font=("Arial", 12),bg="grey",fg="black").pack(side=TOP)
    campus.set("Selecione o Campus")
    itensCampos = {"Irajá","Penha","Duque de Caxias","Nova América","Centro RJ"}
    OptionMenu(LFrom, campus, "Irajá","Penha","Duque de Caxias","Nova América","Centro RJ").pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Período ", font=("Arial", 12), bg="grey", fg="black").pack(side=TOP)
    periodo.set("Selecione o Período")
    itensperiodo = {"1-Primeiro", "2-Segundo", "3-Terceiro", "4-Quarto", "5-Quinto", "6-Sexto"}
    OptionMenu(LFrom, periodo, "1-Primeiro", "2-Segundo", "3-Terceiro", "4-Quarto", "5-Quinto", "6-Sexto").pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="AV1 ", font=("Arial", 12),bg="grey",fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=av1).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="AV2 ", font=("Arial", 12), bg="grey", fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=av2).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="AV3 ", font=("Arial", 12), bg="grey", fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=av3).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="AVD ", font=("Arial", 12), bg="grey", fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=avd).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="AVDS ", font=("Arial", 12), bg="grey", fg="black").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"), textvariable=avds).pack(side=TOP, padx=10, fill=X)

# Botão de ação para cadastrar o aluno
    Button(LFrom, text="Cadastrar", font=("Arial", 14, "bold"), command=Cadastrar, bg="orange", fg="black").pack(side=TOP, padx=15, pady=30, fill=X)

# Criar a opção de pesquisa no frame lateral
    lbl_pesquisa = Label(LeftViewForm, text=" Digite um nome para pesquisar ", font=('Arial', 11), bg="dark grey", fg='white')
    lbl_pesquisa.pack()

# Criando o campo para entrada da pesquisa
    pesquisa = Entry(LeftViewForm, textvariable=SEARCH, font=('Arial', 15), width=10)
    pesquisa.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_pesquisa = Button(LeftViewForm, text="Pesquisar", font=("Arial", 12, 'bold'), command=Pesquisa,bg="orange")
    btn_pesquisa.pack(side=TOP, padx=10, pady=10, fill=X)

# Criando o botão de visualização
    btn_visualizar = Button(LeftViewForm, text="Visualizar Tudo", font=("Arial", 12, 'bold'), command=Visualizar,bg="orange")
    btn_visualizar.pack(side=TOP, padx=10, pady=10, fill=X)

# Limpar todos os campos
    btn_limpar = Button(LeftViewForm, text="Limpar", font=("Arial", 12, 'bold'), command=Limpar,bg="orange")
    btn_limpar.pack(side=TOP, padx=10, pady=10, fill=X)

# Criar o botão de Apagar
    btn_excluir = Button(LeftViewForm, text="Excluir", font=("Arial", 12, 'bold'), command=Excluir,bg="orange")
    btn_excluir.pack(side=TOP, padx=10, pady=10, fill=X)

# Criar o botão de atualizar
    btn_atualizar = Button(LeftViewForm, text="Atualizar", font=("Arial", 12, 'bold'), command=Atualizar,bg="orange")
    btn_atualizar.pack(side=TOP, padx=10, pady=10, fill=X)

# Criar o botão de Sair
    btn_sair = Button(LeftViewForm, text="Sair", font=("Arial", 12, 'bold'), command=janela.destroy, bg="orange")
    btn_sair.pack(side=TOP, padx=10, pady=10, fill=X)

# Configurando o ScroolBar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("ID Aluno","Matricula","Nome","Email","Endereco","Campus","Periodo","AV1","AV2","AV3","AVD","AVDS"),
                        selectmode="extended", height=50, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=BOTH)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=BOTH)
# Configurando os cabeçalhos das colunas
    tree.heading('ID Aluno', text="ID Aluno", anchor=W)
    tree.heading('Matricula', text="Matrícula", anchor=W)
    tree.heading('Nome', text="Nome", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Endereco', text="Endereço", anchor=W)
    tree.heading('Campus', text="Campus", anchor=W)
    tree.heading('Periodo', text="Periodo", anchor=W)
    tree.heading('AV1', text="AV1", anchor=W)
    tree.heading('AV2', text="AV2", anchor=W)
    tree.heading('AV3', text="AV3", anchor=W)
    tree.heading('AVD', text="AVD", anchor=W)
    tree.heading('AVDS', text="AVDS", anchor=W)
# Configurando a largura das colunas
    tree.column('#0', stretch=NO, minwidth=0, width=0)      # espaço inicio
    tree.column('#1', stretch=NO, minwidth=20, width=60)    # id
    tree.column('#2', stretch=NO, minwidth=0, width=70)     # matricula
    tree.column('#3', stretch=NO, minwidth=0, width=150)    # nome
    tree.column('#4', stretch=NO, minwidth=0, width=150)    # email
    tree.column('#5', stretch=NO, minwidth=0, width=250)    # endereço
    tree.column('#6', stretch=NO, minwidth=0, width=150)    # campus
    tree.column('#7', stretch=NO, minwidth=0, width=100)    # período
    tree.column('#8', stretch=NO, minwidth=0, width=35)     # av1
    tree.column('#9', stretch=NO, minwidth=0, width=35)     # av2
    tree.column('#10', stretch=NO, minwidth=0, width=35)    # av3
    tree.column('#11', stretch=NO, minwidth=0, width=35)    # avd
    tree.column('#12', stretch=NO, minwidth=0, width=35)    # avds
    tree.pack()
    Visualizar()

# Função Atualizar Dados do Aluno
def Atualizar():
    criar_tabela()
    if not tree.selection():
        tkMessageBox.showinfo("Atenção!", "Nenhum item selecionado para Atualizar")
    matricula1 = matricula.get()
    nome1 = nome.get()
    email1 = email.get()
    endereco1 = endereco.get()
    campus1 = campus.get()
    periodo1 = periodo.get()
    av11 = av1.get()
    av21 = av2.get()
    av31 = av3.get()
    avd1 = avd.get()
    avds1 = avds.get()
    itemAtual = tree.focus()
    conteudo = (tree.item(itemAtual))
    itemSelecionado = conteudo['values']
    conn.execute("UPDATE TB_ESCOLA SET matricula=?,nome=?,email=?,endereco=?,campus=?,periodo=?,av1=?,av2=?,av3=?,avd=?,avds=? WHERE id_aluno = ?", (matricula1,nome1,email1,endereco1,campus1,periodo1,av11,av21,av31,avd1,avds1,itemSelecionado[0]))
    conn.commit()
    tkMessageBox.showinfo("Mensagem: ", "Cadastro Atualizado com sucesso!")
    Limpar()
    Visualizar()
    conn.close()

def Cadastrar():
    criar_tabela()
    matricula1=matricula.get()
    nome1=nome.get()
    email1=email.get()
    endereco1=endereco.get()
    campus1=campus.get()
    periodo1=periodo.get()
    av11=av1.get()
    av21=av2.get()
    av31=av3.get()
    avd1=avd.get()
    avds1=avds.get()
    if matricula1 != "" and nome1 != "" and email1 != "" and endereco1 != "":
        conn.execute(
            "INSERT INTO TB_ESCOLA (matricula,nome,email,endereco,campus,periodo,av1,av2,av3,avd,avds) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
            (matricula1, nome1, email1, endereco1, campus1, periodo1, av11, av21, av31, avd1, avds1));
        conn.commit()
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        tkMessageBox.showinfo("Mensagem: ", "Aluno Cadastrado com Sucesso!")
        Limpar()
    else:
        tkMessageBox.showinfo("Aviso!", "Campos Obrigatórios Vazio!")
    Visualizar()
    conn.close()

# Função Limpar Campos
def Limpar():
    tree.delete(*tree.get_children())
    Visualizar()
    SEARCH.set("")
    matricula.set("")
    nome.set("")
    email.set("")
    endereco.set("")
    campus.set("")
    periodo.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")

# Função excluir registro selecionado
def Excluir():
    criar_tabela()
    if not tree.selection():
        tkMessageBox.showinfo("Atenção!", "Nenhum item selecionado para excluir")
    else:
        resultado = tkMessageBox.askquestion("Confirmação!", "Tem certeza que deseja excluir este registro?", icon="warning")
        if resultado == "yes":
            itemAtual = tree.focus()
            conteudo = (tree.item(itemAtual))
            itemSelecionado = conteudo['values']
            tree.delete(itemAtual)
            cursor = conn.execute("DELETE FROM TB_ESCOLA WHERE id_aluno = %d" % itemSelecionado[0])
            conn.commit()
            cursor.close()
            conn.close()
            Limpar()

def Pesquisa():
    #open database
    criar_tabela()
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        cursor=conn.execute("SELECT * FROM TB_ESCOLA WHERE nome LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
    else:
        tkMessageBox.showinfo("Aviso!", "Campo Vazio! Para pesquisar digite o termo para pesquisa no campo em branco.")

def Visualizar():
    criar_tabela()
    tree.delete(*tree.get_children())
    cursor = conn.execute("SELECT * FROM TB_ESCOLA")
    busca = cursor.fetchall()
    for dados in busca:
        tree.insert('', 'end', values=(dados))
        tree.bind("<Double-1>",DuploClique)
    cursor.close()
    conn.close()

# Função duplo clique
def DuploClique(self):
    itemAtual = tree.focus()
    conteudo = (tree.item(itemAtual))
    itemSelecionado = conteudo['values']
    matricula.set(itemSelecionado[1])
    nome.set(itemSelecionado[2])
    email.set(itemSelecionado[3])
    endereco.set(itemSelecionado[4])
    campus.set(itemSelecionado[5])
    periodo.set(itemSelecionado[6])
    av1.set(itemSelecionado[7])
    av2.set(itemSelecionado[8])
    av3.set(itemSelecionado[9])
    avd.set(itemSelecionado[10])
    avds.set(itemSelecionado[11])

#calling function
JanelaPrincipal()

if __name__=='__main__':
    mainloop()