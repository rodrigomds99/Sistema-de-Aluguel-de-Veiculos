from tkinter import *
from customtkinter import *
import TelaCadastroClientes
from tkinter import ttk
import database
from datetime import date
from tkinter import messagebox
import TelaPrincipal

db = database.DataBase_Veiculos()

class TelaAluguel:
    def __init__(self):
        self.janela = CTk()
        self.tema()
        self.tela()
        self.frames()
        self.labels()
        self.entradas()
        self.botoes()
        self.treeview()
        self.listar_veiculos()

        self.janela.mainloop()

    def tema(self):
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

    def tela(self):
        self.janela.title("Aluguel")
        self.janela.geometry("1280x720")
        self.janela.resizable(False, False)

    def labels(self):
        self.dataL = CTkLabel(self.janela, text="Data de Locação", font=("Arial", 24))
        self.dataL.place(x=70, y=25)
        self.dataD = CTkLabel(self.janela, text="Data de Devolução", font=("Arial", 24))
        self.dataD.place(x=710, y=25)
        self.informar = CTkLabel(self.janela, text="Tabela de veículos: ", font=("Arial", 24))
        self.informar.place(x=70, y=100)
    def frames(self):
        self.frame_inferior = CTkFrame(self.janela, width=1050, height=300)
        self.frame_inferior.place(x=70, y=150)

    def entradas(self):
        self.entryL = CTkEntry(self.janela, width=350, placeholder_text="Digite a Data de Locação...", font=("Arial", 20))
        self.entryL.place(x=70, y=55)
        self.entryL.bind('<KeyRelease>', lambda event: self.FormatarData(event, self.entryL))

        self.entryD = CTkEntry(self.janela, width=350, placeholder_text="Digite a Data de Devolução...", font=("Arial", 20))
        self.entryD.place(x=710, y=55)
        self.entryD.bind('<KeyRelease>', lambda event: self.FormatarData(event, self.entryD))

    def botoes(self):
        self.confirmar = CTkButton(self.janela, text="Confirmar", font=("Arial", 24), corner_radius=32, hover_color="black", width=150, command=self.Valor_Total)
        self.confirmar.place(x=1100, y=660)
        self.voltar = CTkButton(self.janela,text="Voltar", font=("Arial", 24), corner_radius=32, hover_color="black", width=150, command=self.Voltar_Cadastro_Cliente)
        self.voltar.place(x=70, y=660)

    def treeview(self):
        self.scrollbary = Scrollbar(self.frame_inferior, orient=VERTICAL)

        self.tree = ttk.Treeview(self.frame_inferior, columns=("Tipo", "Modelo", "Marca", "Alugado", "Ano", "Placa", "KM Rodados", "Diária"),
                                 selectmode="extended", height=20, yscrollcommand=self.scrollbary.set)
        self.scrollbary.config(command=self.tree.yview)
        self.scrollbary.pack(side=RIGHT, fill=Y)

        self.tree.heading('Tipo', text="Tipo", anchor=CENTER)
        self.tree.heading('Modelo', text="Modelo", anchor=CENTER)
        self.tree.heading('Marca', text="Marca", anchor=CENTER)
        self.tree.heading('Alugado', text="Alugado", anchor=CENTER)
        self.tree.heading('Ano', text="Ano", anchor=CENTER)
        self.tree.heading('Placa', text="Placa", anchor=CENTER)
        self.tree.heading('KM Rodados', text="KM Rodados", anchor=CENTER)
        self.tree.heading('Diária', text="Diária", anchor=CENTER)

        self.tree.column('#0', stretch=NO, minwidth=0, width=0, anchor=CENTER)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100, anchor=CENTER)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100, anchor=CENTER)
        self.tree.column('#5', stretch=NO, minwidth=0, width=100, anchor=CENTER)
        self.tree.column('#6', stretch=NO, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#7', stretch=NO, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#8', stretch=NO, minwidth=0, width=150, anchor=CENTER)

        self.tree.pack()

    def FormatarData(self, event, entry):
        data_texto = entry.get()
        self.data = ''.join(filter(str.isdigit, data_texto))
        self.data = self.data[:8]

        if len(self.data) <= 2:
            data_formatada = self.data
        elif len(self.data) <= 4:
            data_formatada = f'{self.data[:2]}/{self.data[2:]}'
        else:
            data_formatada = f'{self.data[:2]}/{self.data[2:4]}/{self.data[4:]}'

        entry.delete(0, END)
        entry.insert(0, data_formatada)

    def calcular_dias(self):
        data_completa_locacao = self.entryL.get()
        data_completa_devolucao = self.entryD.get()

        if not data_completa_locacao or not data_completa_devolucao:
            return

        dia_locacao, mes_locacao, ano_locacao = map(int, data_completa_locacao.split('/'))
        dia_devolucao, mes_devolucao, ano_devolucao = map(int, data_completa_devolucao.split('/'))
        data_locacao = date(ano_locacao, mes_locacao, dia_locacao)
        data_devolucao = date(ano_devolucao, mes_devolucao, dia_devolucao)
        dias = data_devolucao - data_locacao
        return dias.days

    def obter_valor_diaria(self):
        selecionado = self.tree.selection()[0]
        valores = self.tree.item(selecionado, 'values')

        diaria_str = valores[7].replace("R$", "").strip()
        diaria = float(diaria_str)

        return diaria

    def Valor_Total(self):
        dias = self.calcular_dias()
        diaria = self.obter_valor_diaria()

        selecionado = self.tree.selection()[0]
        self.valores = self.tree.item(selecionado, 'values')
        placa_veiculo = self.valores[5]

        if self.valores[3] == 'Sim':
            messagebox.showerror(title='Veículo Indisponível', message="Esse veículo já está alugado")
        else:
            self.valor_total = (dias + 1) * diaria
            messagebox.showinfo(title="Valor Total",
                                message=f"Veículo alugado por {dias + 1} dias\nTotal a pagar: R${self.valor_total:.2f}")
            db.conecta_bd()
            db.cursor.execute("UPDATE Veiculos SET Alugado = ? WHERE Placa = ?", ('Sim', placa_veiculo))
            db.conn.commit()

            self.ListarAluguel()
            self.listar_veiculos()

            self.VoltarTelaPrincipal()

    def listar_veiculos(self):
        self.tree.delete(*self.tree.get_children())
        db.conecta_bd()
        db.cursor.execute("SELECT * FROM Veiculos ORDER BY Código ASC")
        self.lista = db.cursor.fetchall()

        for data in self.lista:
            self.tree.insert('', 'end', values=(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))

    def ListarAluguel(self):
        self.modelo = self.valores[1]
        self.placa = self.valores[5]
        self.dataL = self.entryL.get()
        self.dataD = self.entryD.get()

        db.cursor.execute("""
        INSERT INTO Alugueis(Modelo, Placa, DataLocação, DataDevolução, Valor) VALUES(?, ?, ?, ?, ?)
        """, (self.modelo, self.placa, self.dataL, self.dataD, self.valor_total))
        db.conn.commit()

    def VoltarTelaPrincipal(self):
        self.janela.destroy()
        TelaPrincipal.TelaPrincipal()

    def Voltar_Cadastro_Cliente(self):
        self.janela.destroy()
        TelaCadastroClientes.TelaCadastroClientes()

if __name__ == "__main__":
    TelaAluguel()