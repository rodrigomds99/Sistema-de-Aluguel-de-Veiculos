from customtkinter import *
import TelaPrincipal
from tkinter import messagebox
import database

db = database.DataBase_Veiculos()


class TelaCadastroVeiculos:
    def __init__(self):
        self.janela = CTk()
        self.tema()
        self.tela()
        self.Frame()
        self.Labels()
        self.Entradas()
        self.Botoes()

        self.janela.mainloop()

    def tema(self):
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

    def tela(self):
        self.janela.title("Cadastro de Veículos")
        self.janela.geometry("1280x720")
        self.janela.resizable(False,False)

    def Frame(self):
        self.frame = CTkFrame(self.janela, width=640, height=720)
        self.frame.pack(side=RIGHT)

        self.fonte = ("Arial", 24)
        self.fonte_text = ("Arial", 20)

    def Labels(self):
        self.tipo = CTkLabel(self.janela, text="Tipo", font=self.fonte)
        self.tipo.place(x=70, y=25)

        self.marca = CTkLabel(self.janela, text="Marca", font=self.fonte)
        self.marca.place(x=70, y=125)

        self.modelo = CTkLabel(self.janela, text="Modelo", font=self.fonte)
        self.modelo.place(x=70, y=225)

        self.alugado = CTkLabel(self.janela, text="Alugado", font=self.fonte)
        self.alugado.place(x=70, y=325)

        self.placa = CTkLabel(self.frame, text="Placa", font=self.fonte)
        self.placa.place(x=70, y=25)

        self.kmRodados = CTkLabel(self.frame, text="KM Rodados", font=self.fonte)
        self.kmRodados.place(x=370, y=25)

        self.valor = CTkLabel(self.frame, text="Valor da Diária", font=self.fonte)
        self.valor.place(x=70, y=125)

        self.ano = CTkLabel(self.frame, text="Ano", font=self.fonte)
        self.ano.place(x=370, y=125)

    def Entradas(self):
        self.tipo1 = CTkEntry(self.janela, placeholder_text="Digite o tipo do veículo...",width=500)
        self.tipo1.place(x=70, y=55)

        self.marca1 = CTkEntry(self.janela, placeholder_text="Digite a marca do veículo...",width=500)
        self.marca1.place(x=70, y=155)

        self.modelo1 = CTkEntry(self.janela, placeholder_text="Digite o modelo do veículo...",width=500)
        self.modelo1.place(x=70, y=255)

        self.placa1 = CTkEntry(self.frame, placeholder_text="Digite a placa do veículo...", width=200)
        self.placa1.place(x=70, y=55)
        self.placa1.bind('<KeyRelease>', self.FormatarPlaca)

        self.kmRodados1 = CTkEntry(self.frame, placeholder_text="Digite a quilometragem...", width=200)
        self.kmRodados1.place(x=370, y=55)

        self.valor1 = CTkEntry(self.frame, placeholder_text="Digite o valor da diária...", width=200)
        self.valor1.place(x=70, y=155)
        self.valor1.bind('<KeyRelease>', self.FormatarDinheiro)


        self.ano1 = CTkEntry(self.frame, placeholder_text="Digite o ano do veículo...", width=200)
        self.ano1.place(x=370, y=155)
        self.ano1.bind('<KeyRelease>', self.FormatarAno)

        self.alugado1 = CTkEntry(self.janela, placeholder_text="Digite [SIM/NÃO]", width=200)
        self.alugado1.place(x=70, y=355)


    def Botoes(self):
        self.salvar = CTkButton(self.frame, text="Salvar", font=self.fonte, corner_radius=32, hover_color="black", width=150, command=self.adicionar_veiculos)
        self.salvar.place(x=420, y=660)

        self.voltar = CTkButton(self.janela, text="Voltar", font=self.fonte, corner_radius=32, hover_color="black", width= 150, command=self.Voltar)
        self.voltar.place(x=70, y=660)

    def Voltar(self):
        self.janela.destroy()
        TelaPrincipal.TelaPrincipal()


    def FormatarPlaca(self, event):
        placa_input = self.placa1.get()
        placa_input = placa_input[:7]

        placa = placa_input.upper()

        self.placa1.delete(0, END)
        self.placa1.insert(0, placa)

    def FormatarDinheiro(self, event):
        valor_input = self.valor1.get()
        valor_input = ''.join(filter(str.isdigit, valor_input))

        if valor_input and valor_input[0].isdigit():
            valor_formatado = "{:,.2f}".format(float(valor_input) / 100).replace(",", ".")
            valor_formatado = valor_formatado[:-3] + "." + valor_formatado[-2:]
            valor_formatado = "R$ " + valor_formatado
            self.valor1.delete(0, END)
            self.valor1.insert(0, valor_formatado)
        else:
            self.valor1.delete(0, END)

    def FormatarAno(self, event):
        ano_input = self.ano1.get()
        ano_input = ano_input[:4]

        self.ano1.delete(0, END)
        self.ano1.insert(0, ano_input)


    def adicionar_veiculos(self):
        self.tipo = self.tipo1.get()
        self.modelo = self.modelo1.get()
        self.marca = self.marca1.get()
        self.ano = self.ano1.get()
        self.placa = self.placa1.get()
        self.diaria = self.valor1.get()
        self.km = self.kmRodados1.get()
        self.alugado = self.alugado1.get()

        db.conecta_bd()

        if (self.tipo == "" or self.modelo == "" or self.marca == "" or self.ano == "" or self.placa == "" or self.km =="" or self.diaria == "" or self.alugado == ""):
            messagebox.showerror(title="Register Error", message="Preencha Todos os Campos!!")
        else:
            db.cursor.execute("""
            INSERT INTO Veiculos(Tipo, Marca, Modelo, Alugado, Ano, Placa, KM, Diaria) VALUES(?, ?, ?, ?, ?, ?, ?, ?)
            """, (self.tipo, self.marca, self.modelo, self.alugado, self.ano, self.placa, self.km, self.diaria))
            db.conn.commit()
            messagebox.showinfo(title="Cadastro de Veículo", message="Veículo Cadastrado com Sucesso")

            self.janela.destroy()
            TelaPrincipal.TelaPrincipal()


if __name__ == "__main__":
    TelaCadastroVeiculos()