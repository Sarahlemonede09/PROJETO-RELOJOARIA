import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import Label , Entry, Button, Grid , Menu , PhotoImage,  messagebox, Canvas, Scrollbar, VERTICAL,RIGHT

janela = ttk.Window(themename="cyborg")

janela.title("relojoaria")

janela.iconbitmap("favicon.ico")

janela.state("zoomed")

janela.columnconfigure(0, weight=2)

janela.rowconfigure([0, 1, 2, 3, 4, 5, 6], weight=2)

#variaveis globais

entrada_nome = None
entrada_cpf = None
entrada_email = None
entrada_senha = None
regcliente = None
entrada_nomes = None
entrada_parcelas = None
test_ultimacompra = None
entrada_devendo = None
entrada_telefones = None
entrada_emails = None
entrada_precos = None
novoprecos = None

usuarios =[]

clientes_registro = []

quantidade = [11,15,20,25,30,35,40,45]

precos = [219.00, 137.00, 678.00, 100.00, 321.54, 200.00, 156.00, 277.00] 
iamgens_detalhes = ["IMG/relogio-white.png","IMG/relogio-white.png","IMG/relogio-white.png","IMG/relogio-white.png","IMG/relogio-white.png","IMG/relogio-white.png","IMG/relogio-white.png","IMG/relogio-white.png"]
nomeee = ["Relógio Tommy Hilfiger Duncan Masculino Couro Marrom - 1710643", "Relógio Tommy Hilfiger Masculino Borracha Azul 1710595","Relógio Life Colors Feminino Couro Rosa","Relógio Vivara Mata Atlântica Feminino Dourado com Couro", "Relógio Vivara Biomas Tuiuiu Masculino Couro Preto","Relógio Locman Ducati Preto", "Relógio Akium Masculino Couro Preto e Laranja","Relógio Locman Ducati Preto e Vermelho"]
Descricao = ["Cod : TO00004864","Cód : LI00000031", "Cód : VI00000367", "Cód : VI00000350", "Cód : LO00001371", "Cód : AK00003045", "Cód : LO00001366" ]
garantia = ["Garantia : 24 meses","Garantia : 12 meses","Garantia :33 meses","Garantia : 12 meses","Garantia :12 meses","Garantia : 22 meses","Garantia : 12 meses","Garantia : 24 meses"]
clientes = []


def criar_tela_login():
    for widget in janela.winfo_children():
        widget.destroy()

    Label_login = Label(janela, text="LOGIN", font="Montserrat 60", height=2 )
    Label_login.grid(row=0, column=0, columnspan=2, pady=(15,15))

    logo = PhotoImage(file="IMG/login.png")
    logo = logo.subsample(5, 5)
    label = Label(janela, image=logo)
    label.image = logo 
    label.grid(row=0, column=0, pady=(350,0))

    Label_matricula = Label(janela, text="NOME", font="Montserrat 12", height=0)
    Label_matricula.grid(row=2, column=0, padx=0, pady=0)
    matricula = ttk.Entry(janela, width=30 , justify="center")
    matricula.grid(row=2, column=0, padx=10, pady=(60,0))


    Label_senha = Label(janela, text="SENHA",font="Montserrat 12", height=1)
    Label_senha.grid(row=3, column=0,  padx=10, pady=0)
    senha = ttk.Entry(janela, width=30 , justify="center", show="*")
    senha.grid(row=3, column=0, padx=10, pady=(60,0))

#Verificar
    
#----------------------------------------------------------------------------------------------------------

    def Verificar():

        matricula_texto = matricula.get()
        senha_texto = senha.get()


        for usuari in usuarios:
                    if usuari[0] == matricula_texto and usuari[3] == senha_texto:  
                        messagebox.showinfo("Login", "Login bem-sucedido!")
                        menu()

#O outro esta la embaixo




#----------------------------------------------------------------------------------------------------------


    def menu():
  
        M = matricula.get()
        S = senha.get()
        print("Matricula:", M)
        print("Senha:", S)
        menu = ttk.Toplevel(janela)
        menu.title("Menu")
        menu.iconbitmap("favicon.ico")
        menu.state("zoomed")
        menu.grid_columnconfigure(0, weight=1) 
        menu.grid_rowconfigure(0, weight=1)
        janela.rowconfigure([0, 1, 2, 3, 4, 5, 6,7,8,9,10], weight=2)
        menu.grid_columnconfigure(0, weight=1)
        menu.grid_columnconfigure(1, weight=1)
        menu.grid_columnconfigure(2, weight=1)
        menu.grid_columnconfigure(3, weight=1)
        menu.grid_columnconfigure(4, weight=1)
        menu.grid_rowconfigure(0, weight=1)
        menu.grid_rowconfigure(1, weight=1)

        logo = PhotoImage(file="IMG/relogio.png")
        logo = logo.subsample(3, 3)
        label = Label(menu, image=logo)
        label.image = logo  
        label.grid(row=0, column=0, columnspan=5, pady=20)

        button_estoque = ttk.Button(menu, text="Estoque", bootstyle="info", command=estoques,width=20,padding=10)
        button_estoque.grid(row=1, column=1, pady=30, padx=10)

        button_cliente = ttk.Button(menu, text="Cliente", bootstyle="warning", command=clientes,width=20,padding=10)
        button_cliente.grid(row=1, column=3, pady=30, padx=10)
       
#Botões

    button_login = ttk.Button(janela, text="Login", bootstyle="primary", command=Verificar) 
    button_login.grid(row=5, column=0, pady=20)
    button_conta = ttk.Button(janela, text="Criar conta", bootstyle="secondary", command=cadastro)
    button_conta.grid(row=6, column=0, pady=20)



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Essa funcão valida apenas números

def apenas_numeros(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False


# O "P" é uma substituição que se consiste no valor da entrada após a modificação. Resumindo é o texto depois de sofrer a modificação. 
# Ele garante que a função verifique o conteúdo final da caixa de texto após a mudança. 


def cadastro():
    for widget in janela.winfo_children():
        widget.destroy()

    nova_pagina = ttk.Toplevel(janela)
    nova_pagina.title("relojoaria")
    nova_pagina.iconbitmap("favicon.ico")
    nova_pagina.state("zoomed")

    nova_pagina.grid_columnconfigure(0, weight=1) 
    nova_pagina.grid_rowconfigure(0, weight=1)
    janela.rowconfigure([0, 1, 2, 3, 4, 5, 6,7,8,9,10], weight=2)

    Label_cadastro = Label(nova_pagina, text="CADASTRAR", font="Montserrat 60", height=0)
    Label_cadastro.grid(row=0, column=0, padx=10, pady=0)

    logo = PhotoImage(file="IMG/cadastro.png")
    logo = logo.subsample(9, 9)
    label = Label(nova_pagina, image=logo)
    label.image = logo 
    label.grid(row=0, column=0, pady=(200,0))
    
    global entrada_nome, entrada_cpf, entrada_email, entrada_senha


    Label_nome = Label(nova_pagina, text="NOME COMPLETO", font="Montserrat 12", height=0)
    Label_nome.grid(row=1, column=0, padx=10, pady=10)
    entrada_nome = ttk.Entry(nova_pagina, width=30)
    entrada_nome.grid(row=2, column=0, padx=10, pady=10)

    Label_cpf = Label(nova_pagina, text="CPF", font="Montserrat 12", height=0)
    Label_cpf.grid(row=3, column=0, padx=10, pady=10)
    validate_cpf = nova_pagina.register(apenas_numeros)
    entrada_cpf = ttk.Entry(nova_pagina, width=30,validate="key", validatecommand=(validate_cpf, "%P"))#O validatecommand define uma função de validação para entradas de texto
    entrada_cpf.grid(row=4, column=0, padx=10, pady=10)

    Label_email = Label(nova_pagina, text="EMAIL", font="Montserrat 12", height=0)
    Label_email.grid(row=5, column=0, padx=10, pady=10)
    entrada_email = ttk.Entry(nova_pagina, width=30)
    entrada_email.grid(row=6, column=0, padx=10, pady=10)

    Label_senha = Label(nova_pagina, text="SENHA", font="Montserrat 12", height=0)
    Label_senha.grid(row=7, column=0, padx=10, pady=10)
    entrada_senha = ttk.Entry(nova_pagina, width=30, show="*")
    entrada_senha.grid(row=8, column=0, padx=10, pady=10)

    def fazer_cadastro():
        matricula = entrada_nome.get()
        cpf = entrada_cpf.get()
        email = entrada_email.get()
        senha = entrada_senha.get()

        print("Matrícula:", matricula)
        print("CPF:", cpf)
        print("Email:", email)
        print("Senha:", senha)

        if not matricula or not cpf or not email or not senha:
            messagebox.showwarning("AVISO", "Todos os campos devem ser preenchidos")
        elif len(senha) < 5:
            messagebox.showerror("AVISO", "A senha tem que conter no minimo 5 carcteres")
        elif "@" not in email:
            messagebox.showerror("AVISO","Email precisa ter '@' ")
        elif".com" not in email:
            messagebox.showerror("AVISO","Email precisa ter '.com' ")
        elif len(cpf) != 11:
            messagebox.showerror("AVISO","CPF aceita a entrada de apenas 11 dígitos.' ")
        else:
          usuarios.append([matricula, cpf, email, senha])
          messagebox.showinfo("AVISO", "Cadastro feito com sucesso")
          criar_tela_login()
        #volta login
        criar_tela_login()
        

    # Botões
    button_cadastrar = ttk.Button(nova_pagina, text="Cadastrar", bootstyle="primary", command=fazer_cadastro)
    button_cadastrar.grid(row=10, column=0, pady=20)

    button_voltar = ttk.Button(nova_pagina, text="Voltar", bootstyle="secondary", command=criar_tela_login)
    button_voltar.grid(row=11, column=0, pady=10)



# Inicializa a aplicação na tela de login
criar_tela_login()



#------------------------------------CALCULOS-----------------------------------------------------------------------------------------------------------------------------------------#

soma = 0 
menos = 0 

def soma(indice):
    global quantidade
    quantidade[indice] += 1
    atualizarvalor()
    urgencia()

def menos(indice):
    global quantidade
    if quantidade[indice] > 10:
        quantidade[indice] -= 1
    else:
        messagebox.showwarning(
            "Estoque Insuficiente",
            f"Não é possível reduzir a quantidade abaixo de 10 para o item {indice + 1}. Estoque atual: {quantidade[indice]}"
        )
    atualizarvalor()
    urgencia()


def atualizarvalor():
    for i, quant in enumerate(quantidade):
        quantidade_labels[i].config(text=f"Quantidade: {quant}")
        urgencia()


def urgencia():
    for i, quant in enumerate(quantidade):
        print(f"Item {i + 1}: {quant}")  # Verifique se os valores estão corretos
        if quant < 10:
            messagebox.showwarning(
                "Alerta de Estoque Baixo",
                f"Item {i + 1} está com estoque baixo (Quantidade: {quant})."
            )
            break

def calcular_total():
    total = sum(quantidade) #o sum faz a soma de todos os elementos
    messagebox.showinfo("Total no Estoque", f"Total de itens no estoque: {total}")

def calcular_valortotal():
    total = sum(precos) #o sum faz a soma de todos os elementos
    messagebox.showinfo("Valor total no estoque", f"Preço total de itens no estoque: {total}")

quantidade_labels = []

def somapreco(indice):
    global precos
    precos[indice] += 1

def menospreco(indice):
    global precos
    precos[indice] -= 1


#Páginas
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Estoque
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------






def estoques():


    estoque = ttk.Toplevel(janela)
    estoque.title("Estoque")
    estoque.iconbitmap("favicon.ico")
    estoque.state("zoomed")
    estoque.configure(bg="#000000")

    estoque.grid_columnconfigure(0, weight=1) 
    estoque.grid_columnconfigure(1, weight=1)
    estoque.grid_columnconfigure(2, weight=1)
    estoque.grid_columnconfigure(3, weight=1)
    estoque.grid_columnconfigure(4, weight=1)


#e so demonstrativo mano, n tem problema
    estoque.grid_rowconfigure(0, weight=0)  
    estoque.grid_rowconfigure(1, weight=0)  

    label_estoque = tk.Label(estoque, text="ESTOQUE", font="Montserrat 60")
    label_estoque.grid(row=0, column=0, columnspan=5, sticky="n", ipadx=1000,pady=(0,30))

    button_total = tk.Button(estoque, text="Total de Itens", command=calcular_total,height=2,width=11)
    button_total.grid(row=1, column=0, padx=(0,300), pady=(0,0))

    button_total = tk.Button(estoque, text="Valor total em Estoque", command=calcular_valortotal,height=2,width=20)
    button_total.grid(row=2, column=0, padx=(0,300), pady=(0,0))
    
    def voltar_para_menu():
        estoque.destroy()

    button_voltar1 = ttk.Button(estoque, text="Voltar", bootstyle="secondary",command=voltar_para_menu, width=5)
    button_voltar1.grid(row=4, column=0, columnspan=5, sticky="n")
    
    
    frame1 = tk.Frame(estoque)
    frame1.grid(row=1, column=0, padx=(140,0))
    frame1.configure(bg="#333333")
    logo1 = PhotoImage(file="IMG/relogio-white.png").subsample(4, 4)
    label_imagem1 = Label(frame1, image=logo1, bd=5, relief="solid", highlightthickness=3, highlightbackground="white")
    label_imagem1.image = logo1
    label_imagem1.pack(pady=(9,0))

    label_imagem1.bind("<Button-1>", lambda event: detalhamento(nomeee[0], Descricao[0], garantia[0], quantidade[0], precos[0]))

    label_nome1 = Label(frame1, text="Relógio A", font="Montserrat 12",relief="solid",highlightthickness=3, highlightbackground="white")
    label_nome1.pack(pady=7,padx=7)

    quantidade_label1 = Label(frame1, text=f"Quantidade: {quantidade[0]}", font="Montserrat 10", relief="solid", highlightthickness=3, highlightbackground="white")
    quantidade_label1.pack(pady=5, padx=7)
    quantidade_labels.append(quantidade_label1)

    button_soma1 = ttk.Button(frame1, text="+", bootstyle="success", command=lambda: soma(0),width=10, padding=10)
    button_soma1.pack(side="left", padx=5, pady=5)
    button_menos1 = ttk.Button(frame1, text="-", bootstyle="danger", command=lambda: menos(0),width=10, padding=10)
    button_menos1.pack(side="right", padx=5, pady=5)



    # Frame 2 (Imagem 2)
    frame2 = tk.Frame(estoque)
    frame2.grid(row=1, column=1, padx=0, pady=20)
    frame2.configure(bg="#333333")
    logo2 = PhotoImage(file="IMG/relogio-white.png").subsample(4, 4)
    label_imagem2 = Label(frame2, image=logo2, bd=5, relief="solid", highlightthickness=3, highlightbackground="white")
    label_imagem2.image = logo2
    label_imagem2.pack(pady=(9,0))

    label_imagem2.bind("<Button-1>", lambda event: detalhamento(nomeee[1], Descricao[1], garantia[1], quantidade[1],precos[1]))
    label_nome2 = Label(frame2, text="Relógio B", font="Montserrat 12",relief="solid",highlightthickness=3, highlightbackground="white")
    label_nome2.pack(pady=7,padx=7)


    quantidade_label2 = Label(frame2, text=f"Quantidade: {quantidade[1]}", font="Montserrat 10", relief="solid", highlightthickness=3, highlightbackground="white")
    quantidade_label2.pack(pady=5, padx=7)
    quantidade_labels.append(quantidade_label2)

    button_soma2 = ttk.Button(frame2, text="+", bootstyle="success", command=lambda: soma(1),width=10, padding=10)
    button_soma2.pack(side="left", padx=5, pady=5)
    button_menos2 = ttk.Button(frame2, text="-", bootstyle="danger", command=lambda: menos(1),width=10, padding=10)
    button_menos2.pack(side="right", padx=5, pady=5)




    # Frame 3 (Imagem 3)
    frame3 = tk.Frame(estoque)
    frame3.grid(row=1, column=2, padx=10, pady=20)
    frame3.configure(bg="#333333")
    logo3 = PhotoImage(file="IMG/relogio-white.png").subsample(4, 4)
    label_imagem3 = Label(frame3, image=logo3, bd=5, relief="solid", highlightthickness=3, highlightbackground="white")
    label_imagem3.image = logo3
    label_imagem3.pack(pady=(9,0))
    label_imagem3.bind("<Button-1>", lambda event: detalhamento(nomeee[2], Descricao[2], garantia[2], quantidade[2],precos[2]))


    label_nome3 = Label(frame3, text="Relógio C", font="Montserrat 12",relief="solid",highlightthickness=3, highlightbackground="white")
    label_nome3.pack(pady=7,padx=7)

    quantidade_label3 = Label(frame3, text=f"Quantidade: {quantidade[2]}", font="Montserrat 10", relief="solid", highlightthickness=3, highlightbackground="white")
    quantidade_label3.pack(pady=5, padx=7)
    quantidade_labels.append(quantidade_label3)

    button_soma3 = ttk.Button(frame3, text="+", bootstyle="success", command=lambda: soma(2),width=10, padding=10)
    button_soma3.pack(side="left", padx=5, pady=5)
    button_menos3 = ttk.Button(frame3, text="-", bootstyle="danger", command=lambda: menos(2),width=10, padding=10)
    button_menos3.pack(side="right", padx=5, pady=5)


    # Frame 4 (Imagem 4)
    frame4 = tk.Frame(estoque)
    frame4.grid(row=1, column=3, padx=10, pady=20)
    frame4.configure(bg="#333333")
    logo4 = PhotoImage(file="IMG/relogio-white.png").subsample(4, 4)
    label_imagem4 = Label(frame4, image=logo4, bd=5, relief="solid", highlightthickness=3, highlightbackground="white")
    label_imagem4.image = logo4
    label_imagem4.pack(pady=(9,0))
    label_imagem3.bind("<Button-1>", lambda event: detalhamento(nomeee[3], Descricao[3], garantia[3], quantidade[3],precos[3]))



    label_nome4 = Label(frame4, text="Relógio D", font="Montserrat 12",relief="solid",highlightthickness=3, highlightbackground="white")
    label_nome4.pack(pady=7,padx=7)

    quantidade_label4 = Label(frame4, text=f"Quantidade: {quantidade[3]}", font="Montserrat 10", relief="solid", highlightthickness=3, highlightbackground="white")
    quantidade_label4.pack(pady=5, padx=7)
    quantidade_labels.append(quantidade_label4)
    button_soma4 = ttk.Button(frame4, text="+", bootstyle="success", command=lambda: soma(3),width=10, padding=10)
    button_soma4.pack(side="left", padx=5, pady=5)
    button_menos4 = ttk.Button(frame4, text="-", bootstyle="danger", command=lambda: menos(3),width=10, padding=10)
    button_menos4.pack(side="right", padx=5, pady=5)

    # Frame 5 (Imagem 5)
    frame5 = tk.Frame(estoque)
    frame5.grid(row=2, column=0, padx=(140,0), pady=(20,20))
    frame5.configure(bg="#333333")
    logo5 = PhotoImage(file="IMG/relogio-white.png").subsample(4, 4)
    label_imagem5 = Label(frame5, image=logo5, bd=5, relief="solid", highlightthickness=3, highlightbackground="white")
    label_imagem5.image = logo5
    label_imagem5.pack(pady=(9,0))
    label_imagem5.bind("<Button-1>", lambda event: detalhamento(nomeee[4], Descricao[4], garantia[4], quantidade[4],precos[4]))
    label_nome5 = Label(frame5, text="Relógio E", font="Montserrat 12",relief="solid",highlightthickness=3, highlightbackground="white")
    label_nome5.pack(pady=7,padx=7)

    quantidade_label5 = Label(frame5, text=f"Quantidade: {quantidade[4]}", font="Montserrat 10", relief="solid", highlightthickness=3, highlightbackground="white")
    quantidade_label5.pack(pady=5, padx=7)
    quantidade_labels.append(quantidade_label5)

    button_soma5 = ttk.Button(frame5, text="+", bootstyle="success", command=lambda: soma(4),width=10, padding=10)
    button_soma5.pack(side="left", padx=5, pady=5)
    button_menos5 = ttk.Button(frame5, text="-", bootstyle="danger", command=lambda: menos(4),width=10, padding=10)
    button_menos5.pack(side="right", padx=5, pady=5)

    # Frame 6 (Imagem 6)
    frame6 = tk.Frame(estoque)
    frame6.grid(row=2, column=1, padx=10, pady=(20,20))
    frame6.configure(bg="#333333")
    logo6 = PhotoImage(file="IMG/relogio-white.png").subsample(4, 4)
    label_imagem6 = Label(frame6, image=logo6, bd=5, relief="solid", highlightthickness=3, highlightbackground="white")
    label_imagem6.image = logo6
    label_imagem6.pack(pady=(9,0))
    label_imagem6.bind("<Button-1>", lambda event: detalhamento(nomeee[5], Descricao[5], garantia[5], quantidade[5],precos[5]))

    

    label_nome6 = Label(frame6, text="Relógio F", font="Montserrat 12",relief="solid",highlightthickness=3, highlightbackground="white")
    label_nome6.pack(pady=7,padx=7)
  
    quantidade_label6 = Label(frame6, text=f"Quantidade: {quantidade[5]}", font="Montserrat 10", relief="solid", highlightthickness=3, highlightbackground="white")
    quantidade_label6.pack(pady=5, padx=7)
    quantidade_labels.append(quantidade_label6)


    button_soma6 = ttk.Button(frame6, text="+", bootstyle="success", command=lambda: soma(5),width=10, padding=10)
    button_soma6.pack(side="left", padx=5, pady=5)
    button_menos6 = ttk.Button(frame6, text="-", bootstyle="danger", command=lambda: menos(5),width=10, padding=10)
    button_menos6.pack(side="right", padx=5, pady=5)


    # Frame 7 (Imagem 7)
    frame7 = tk.Frame(estoque)
    frame7.grid(row=2, column=2, padx=10, pady=(20,20))
    frame7.configure(bg="#333333")
    logo7 = PhotoImage(file="IMG/relogio-white.png").subsample(4, 4)
    label_imagem7 = Label(frame7, image=logo7, bd=5, relief="solid", highlightthickness=3, highlightbackground="white")
    label_imagem7.image = logo7
    label_imagem7.pack(pady=(9,0))
    label_imagem7.bind("<Button-1>", lambda event: detalhamento(nomeee[6], Descricao[6], garantia[6], quantidade[6],precos[6]))
    label_nome7 = Label(frame7, text="Relógio G", font="Montserrat 12",relief="solid",highlightthickness=3, highlightbackground="white")
    label_nome7.pack(pady=7,padx=7)

    quantidade_label7 = Label(frame7, text=f"Quantidade: {quantidade[6]}", font="Montserrat 10", relief="solid", highlightthickness=3, highlightbackground="white")
    quantidade_label7.pack(pady=5, padx=7)
    quantidade_labels.append(quantidade_label7)
    button_soma7 = ttk.Button(frame7, text="+", bootstyle="success", command=lambda: soma(6),width=10, padding=10)
    button_soma7.pack(side="left", padx=5, pady=5)
    button_menos7 = ttk.Button(frame7, text="-", bootstyle="danger", command=lambda: menos(6),width=10, padding=10)
    button_menos7.pack(side="right", padx=5, pady=5)




    # Frame 8 (Imagem 8)
    frame8 = tk.Frame(estoque)
    frame8.grid(row=2, column=3, padx=10, pady=(20,20))
    frame8.configure(bg="#333333")
    logo8 = PhotoImage(file="IMG/relogio-white.png").subsample(4, 4)
    label_imagem8 = Label(frame8, image=logo8, bd=5, relief="solid", highlightthickness=3, highlightbackground="white")
    label_imagem8.image = logo8
    label_imagem8.pack(pady=(9,0))
    label_imagem8.bind("<Button-1>", lambda event: detalhamento(nomeee[7], Descricao[7], garantia[7], quantidade[7],precos[7]))



    label_nome8 = Label(frame8, text="Relógio H", font="Montserrat 12",relief="solid",highlightthickness=3, highlightbackground="white")
    label_nome8.pack(pady=7,padx=7)


    quantidade_label8 = Label(frame8, text=f"Quantidade: {quantidade[7]}", font="Montserrat 10", relief="solid", highlightthickness=3, highlightbackground="white")
    quantidade_label8.pack(pady=5, padx=7)
    quantidade_labels.append(quantidade_label8)
    button_soma8 = ttk.Button(frame8, text="+", bootstyle="success", command=lambda: soma(7),width=10, padding=10)
    button_soma8.pack(side="left", padx=5, pady=5)
    button_menos8 = ttk.Button(frame8, text="-", bootstyle="danger", command=lambda: menos(7),width=10, padding=10)
    button_menos8.pack(side="right", padx=5, pady=5)

    urgencia()
    atualizarvalor()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Detalhes
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def detalhamento(nomeee, Descricao, garantia, quantidade, precos):
    detalhe = ttk.Toplevel(janela)
    detalhe.title("Detalhes")
    detalhe.iconbitmap("favicon.ico")
    detalhe.geometry("800x800")
    detalhe.resizable(False, False)
    detalhe.grid_columnconfigure(0, weight=1) 
    detalhe.grid_rowconfigure(0, weight=1) 

    imagem = PhotoImage(file=iamgens_detalhes[0]).subsample(3, 3)
    label_imagem = tk.Label(detalhe, image=imagem)
    label_imagem.image = imagem
    label_imagem.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    #Coloquei nomes nas labels para ficar com uma visualização mais facil
    
    label_nome = tk.Label(detalhe, text=nomeee, font="Montserrat 18", bg="#333333", fg="white")
    label_nome.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    
    label_descricao = tk.Label(detalhe, text=f"Descrição: {Descricao}", font="Montserrat 12", bg="#333333", fg="white")
    label_descricao.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    
    label_preco = tk.Label(detalhe, text=f"Preço: R$ {precos:.2f}", font="Montserrat 12", bg="#333333", fg="white")
    label_preco.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    
    label_garantia = tk.Label(detalhe, text=f"{garantia}", font="Montserrat 12", bg="#333333", fg="white")
    label_garantia.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    
    label_quantidade = tk.Label(detalhe, text=f"Quantidade disponível: {quantidade}", font="Montserrat 12", bg="#333333", fg="white")
    label_quantidade.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    tk.Button(detalhe, text="Alterar Valor", command=lambda: registrarpreco(label_preco)).grid(row=3, column=0, padx=(0,425), pady=(0,0))
    tk.Button(detalhe, text="Voltar", command=detalhe.destroy).grid(row=6, column=0, padx=10, pady=20, sticky="w")

# Registrar Preco
def registrarpreco(label_preco):
    global novoprecos
    novoprecos = ttk.Toplevel(janela)
    novoprecos.title("Alterar Preço")
    novoprecos.iconbitmap("favicon.ico")
    novoprecos.geometry("500x500+50+50")
    novoprecos.resizable(False, False)

    global entrada_precos

    tk.Label(novoprecos, text="Alterar Preço:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entrada_precos = tk.Entry(novoprecos, width=30)
    entrada_precos.grid(row=0, column=1, padx=10, pady=5)

    button_salvarprecos = ttk.Button(novoprecos, text="Salvar", bootstyle="success", command=lambda: salvarpreco(label_preco))
    button_salvarprecos.grid(row=6, column=0, columnspan=2, pady=10)

def salvarpreco(label_preco):
    novoprecos = entrada_precos.get()
    label_preco.config(text=f"Preço: R$ {float(novoprecos):.2f}")
    print("Preço salvo:", novoprecos)
    
    

#------------------------------------------------------------------------
#Atualizar Preco



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Finanças
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def financas(): 
    

    financas = ttk.Toplevel(janela)
    financas.title("Estoque")
    financas.iconbitmap("favicon.ico")
    financas.state("zoomed")


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Cliente
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------





def clientes(): 
    

    cliente = ttk.Toplevel(janela)
    cliente.title("Área Clientes")
    cliente.iconbitmap("favicon.ico")
    cliente.state("zoomed")
    cliente.configure(bg="#000000")
    
    label_cliente = tk.Label(cliente, text="CLIENTE", font="Montserrat 60")
    label_cliente.grid(row=0, column=0, sticky="n", ipadx=600,padx=(0,0))

    logo = PhotoImage(file="IMG/clients2.png")
    label = Label(cliente, image=logo)
    label.image = logo 
    label.grid(row=0, column=0,padx=(0,500),pady=(100,0))

    logo = PhotoImage(file="IMG/historico.png")
    label = Label(cliente, image=logo)
    label.image = logo 
    label.grid(row=0, column=0,padx=(500,0),pady=(100,0))

    button_cliente = ttk.Button(cliente, text="Cliente", bootstyle="warning",width=10, command=registrarcliente,padding=10)
    button_cliente.grid(row=0, column=0, pady=(450,0), padx=(0,500))

    button_historico = ttk.Button(cliente, text="Historico", bootstyle="warning",width=10,padding=10,command=historicocliente)
    button_historico.grid(row=0, column=0, pady=(450,0), padx=(500,0)) 

    def voltar_para_menu():
        cliente.destroy()


    button_voltar2 = ttk.Button(cliente, text="Voltar", bootstyle="secondary",command=voltar_para_menu, width=5,padding=(20,20))
    button_voltar2.grid(row=0,column=0, pady=(750,0), padx=(0, 0)) 


def registrarcliente():
    global regcliente
    regcliente = ttk.Toplevel(janela)
    regcliente.title("Registro Cliente")
    regcliente.iconbitmap("favicon.ico")
    regcliente.geometry("500x500+50+50")
    regcliente.resizable(False, False)



    global entrada_nomes, entrada_emails, entrada_telefones, test_ultimacompra, entrada_devendo, entrada_parcelas

    tk.Label(regcliente, text="Nome:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    entrada_nomes = tk.Entry(regcliente, width=30)
    entrada_nomes.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(regcliente, text="E-mail:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
    entrada_emails = tk.Entry(regcliente, width=30)
    entrada_emails.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(regcliente, text="Telefone:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
    entrada_telefones = tk.Entry(regcliente, width=30)
    entrada_telefones.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(regcliente, text="Ultima Compra:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
    test_ultimacompra = tk.Entry(regcliente, width=30)
    test_ultimacompra.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(regcliente, text="Devendo:").grid(row=4, column=0, padx=10, pady=5, sticky="w")
    entrada_devendo = tk.Entry(regcliente, width=30)
    entrada_devendo.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(regcliente, text="Parcelas a serem pagas:").grid(row=5, column=0, padx=10, pady=5, sticky="w")
    entrada_parcelas = tk.Entry(regcliente, width=30)
    entrada_parcelas.grid(row=5, column=1, padx=10, pady=5)

    button_salvar = ttk.Button(regcliente, text="Salvar", bootstyle="success", command=salvarcliente)
    button_salvar.grid(row=6, column=0, columnspan=2, pady=10)

def salvarcliente():

    nomes = entrada_nomes.get()
    emails = entrada_emails.get()
    telefones = entrada_telefones.get()
    ultimacompra = test_ultimacompra.get()
    devendo = entrada_devendo.get()
    parcelas = entrada_parcelas.get()

    cliente = [nomes, emails, telefones, ultimacompra, devendo, parcelas]
    clientes_registro.append(cliente)
    print("Cliente salvo:", nomes, emails, telefones, ultimacompra, devendo, parcelas) #mudar isso amanha
    entrada_nomes.delete(0, tk.END)
    entrada_emails.delete(0, tk.END)
    entrada_telefones.delete(0, tk.END)
    test_ultimacompra.delete(0, tk.END)
    entrada_devendo.delete(0, tk.END)
    entrada_parcelas.delete(0, tk.END)
    regcliente.destroy()
        



def historicocliente():

    historico = ttk.Toplevel(janela)
    historico.title("Histórico")
    historico.iconbitmap("favicon.ico")
    historico.geometry("800x800")
    historico.resizable(False, False)


    frame = ttk.Frame(historico)
    frame.pack(fill=tk.BOTH, expand=True)


    canvas = tk.Canvas(frame)
    canvas.pack(side="left", fill="both", expand=True)


    scrollbar_vertical = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    scrollbar_vertical.pack(side=RIGHT, fill=Y)

    scrollbar_horizontal = Scrollbar(frame, orient=HORIZONTAL, command=canvas.xview)
    scrollbar_horizontal.pack(side="bottom", fill=X)


 
    canvas.config(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)



    frame_interno = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=frame_interno, anchor="nw")



#arruma o titulo deixa colado na parade, acho que vai ficar melhor.
    label_historico = tk.Label(frame_interno, text="Histórico", font="Montserrat 20")
    label_historico.grid(row=0, column=0, columnspan=6, pady=20)

    row = 1

    def voltar_para_menu():
        historico.destroy()

    for cliente in clientes_registro:
        tk.Label(frame_interno, text="Nome: " + cliente[0]).grid(row=row, column=0, sticky="w", padx=10, pady=5)
        tk.Label(frame_interno, text="E-mail: " + cliente[1]).grid(row=row, column=1, sticky="w", padx=10, pady=5)
        tk.Label(frame_interno, text="Telefone: " + cliente[2]).grid(row=row, column=2, sticky="w", padx=10, pady=5)
        tk.Label(frame_interno, text="Última Compra: " + cliente[3]).grid(row=row, column=3, sticky="w", padx=10, pady=5)
        tk.Label(frame_interno, text="Devendo: " + cliente[4]).grid(row=row, column=4, sticky="w", padx=10, pady=5)
        tk.Label(frame_interno, text="Parcelas: " + cliente[5]).grid(row=row, column=5, sticky="w", padx=10, pady=5)
        row += 1


    button_voltar_hist = ttk.Button(frame_interno, text="Voltar", bootstyle="secondary", command=voltar_para_menu, width=10)
    button_voltar_hist.grid(row=row, column=0, columnspan=6, pady=20)


    frame_interno.update_idletasks()


    canvas.config(scrollregion=canvas.bbox("all"))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------












# Loop da aplicação
janela.mainloop()
