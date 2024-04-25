from customtkinter import *
from tkinter import messagebox
import TelaAluguel
import TelaPrincipal
import database

db = database.DataBase_Clientes()


class TelaCadastroClientes:
    def __init__(self):
        self.janela = CTk()
        self.tema()
        self.tela()
        self.frame()
        self.botoes()
        self.labels()
        self.entradas()
        self.janela.mainloop()

    def tema(self):
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

    def tela(self):
        self.janela.title("Cadastro de Veículos")
        self.janela.geometry("640x720")
        self.janela.resizable(False,False)

    def frame(self):
        self.frame_1 = CTkFrame(self.janela, width=640, height=720)
        self.frame_1.pack(side=LEFT)

    def botoes(self):
        self.continuar = CTkButton(self.frame_1, text='Continuar', font=('Arial', 24, 'bold'), width=150, corner_radius=32, hover_color="black", command=self.CadastrarClientes)
        self.continuar.place(x=460, y=660)

        self.voltar = CTkButton(self.frame_1, text="Voltar", font=("Arial", 24, "bold"), width=150, corner_radius=32, hover_color="black", command=self.Voltar)
        self.voltar.place(x=30, y=660)

    def labels(self):
        self.lb_nome = CTkLabel(self.frame_1, text='Nome Completo', font=('Arial', 24, 'bold'))
        self.lb_nome.place(x=30, y=25)

        self.lb_cpf = CTkLabel(self.frame_1, text='CPF', font=('Arial', 24, 'bold'))
        self.lb_cpf.place(x=30, y=125)

        self.cnh = CTkLabel(self.frame_1, text='CNH', font=('Arial', 24, 'bold'))
        self.cnh.place(x=30, y=225)

        self.lb_email = CTkLabel(self.frame_1, text='E-mail', font=('Arial', 24, 'bold'))
        self.lb_email.place(x=30, y=325)

        self.lb_telefone = CTkLabel(self.frame_1, text='Telefone', font=('Arial', 24, 'bold'))
        self.lb_telefone.place(x=30, y=425)

        self.lb_cep = CTkLabel(self.frame_1, text='CEP', font=('Arial', 24, 'bold'))
        self.lb_cep.place(x=30, y=525)

    def entradas(self):
        fonte = ("Arial", 18)

        self.entrada_nome = CTkEntry(self.frame_1, width=400, placeholder_text="Digite seu nome completo...", font=fonte)
        self.entrada_nome.place(x=30, y=55)

        self.entrada_cpf = CTkEntry(self.frame_1, width=250, placeholder_text="Digite seu CPF...", font=fonte)
        self.entrada_cpf.place(x=30, y=155)
        self.entrada_cpf.bind('<KeyRelease>', self.FormatarCPF)

        self.entrada_cnh = CTkEntry(self.frame_1, width=250, placeholder_text="Digite sua CNH...", font=fonte)
        self.entrada_cnh.place(x=30, y=255)
        self.entrada_cnh.bind('<KeyRelease>', self.FormatarCNH)

        self.entrada_email = CTkEntry(self.frame_1, width=400, placeholder_text="Digite seu email...", font=fonte)
        self.entrada_email.place(x=30, y=355)

        self.entrada_telefone = CTkEntry(self.frame_1, width=250, placeholder_text="Digite seu telefone...", font=fonte)
        self.entrada_telefone.place(x=30, y=455)
        self.entrada_telefone.bind('<KeyRelease>', self.FormatarTelefone)

        self.entrada_cep = CTkEntry(self.frame_1, width=250, placeholder_text="Digite seu CEP...", font=fonte)
        self.entrada_cep.place(x=30, y=555)
        self.entrada_cep.bind('<KeyRelease>', self.FormatarCEP)


    def FormatarCPF(self, event):
        self.cpf = self.entrada_cpf.get()
        self.cpf = ''.join(filter(str.isdigit, self.cpf))
        self.cpf = self.cpf[:11]

        if len(self.cpf) <= 3:
            cpf_formatado = self.cpf
        elif len(self.cpf) <= 6:
            cpf_formatado = '{}.'.format(self.cpf[:3]) + self.cpf[3:]
        elif len(self.cpf) <= 9:
            cpf_formatado = f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:]}'
        else:
            cpf_formatado = f'{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}'

        self.entrada_cpf.delete(0, END)
        self.entrada_cpf.insert(0, cpf_formatado)

    def FormatarTelefone(self, event):
        self.telefone = self.entrada_telefone.get()
        self.telefone = ''.join(filter(str.isdigit, self.telefone))
        self.telefone = self.telefone[:11]

        if len(self.telefone) > 2:
            if len(self.telefone) <= 2:
                telefone_formatado = f'({self.telefone})'
            elif len(self.telefone) <= 7:
                telefone_formatado = f'({self.telefone[:2]}) {self.telefone[2:]}'
            else:
                telefone_formatado = f'({self.telefone[:2]}) {self.telefone[2:7]}-{self.telefone[7:]}'
        else:
            telefone_formatado = self.telefone

        self.entrada_telefone.delete(0, END)
        self.entrada_telefone.insert(0, telefone_formatado)

    def FormatarCEP(self, event):
        self.cep = self.entrada_cep.get()
        self.cep = ''.join(filter(str.isdigit, self.cep))
        self.cep = self.cep[:8]

        if len(self.cep) <= 5:
            cep_formatado = self.cep
        else:
            cep_formatado = f'{self.cep[:5]}-{self.cep[5:]}'

        self.entrada_cep.delete(0, END)
        self.entrada_cep.insert(0, cep_formatado)

    def FormatarCNH(self, event):
        cnh = self.entrada_cnh.get()
        cnh = ''.join(filter(str.isdigit, cnh))
        cnh = cnh[:11]
        self.entrada_cnh.delete(0, END)
        self.entrada_cnh.insert(0, cnh)

    def Voltar(self):
        self.janela.destroy()
        TelaPrincipal.TelaPrincipal()

    def AlugarVeiculos(self):
        self.janela.destroy()
        TelaAluguel.TelaAluguel()

    def CadastrarClientes(self):
        self.nome = self.entrada_nome.get()
        self.CPF = self.entrada_cpf.get()
        self.CNH = self.entrada_cnh.get()
        self.email = self.entrada_email.get()
        self.telefone = self.entrada_telefone.get()
        self.CEP = self.entrada_cep.get()

        if (self.nome == "" or self.CPF == "" or self.CNH == "" or self.email == "" or self.telefone == "" or self.CEP == ""):
            messagebox.showerror(title="Register Error", message="Preencha Todos os Campos!!")
        else:
            db.cursor.execute("""
            INSERT INTO Clientes(Nome, CPF, CNH, Email, Telefone, CEP) VALUES(?, ?, ?, ?, ?, ?)
            """,(self.nome, self.CPF, self.CNH, self.email, self.telefone, self.CEP))
            db.conn.commit()
            messagebox.showinfo(title="Cadastro de Cliente", message="Cliente Cadastrado com Sucesso!")

            self.AlugarVeiculos()


if __name__ == "_main_":
    TelaCadastroClientes()