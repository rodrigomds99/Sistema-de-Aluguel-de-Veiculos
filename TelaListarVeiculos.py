from tkinter import *
from customtkinter import *
from tkinter import ttk
import TelaPrincipal
import database

db = database.DataBase_Veiculos()

class TelaListarVeiculos:
    def __init__(self):
        self.janela = CTk()
        self.tema()
        self.tela()
        self.botoes()
        self.frames()
        self.treeview()
        self.listar_veiculos()

        self.janela.mainloop()

    def tema(self):
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

    def tela(self):
        self.janela.title("Lista de Veículos")
        self.janela.geometry("1280x720")
        self.janela.resizable(False, False)

    def frames(self):
        self.frame = CTkFrame(self.janela, width=1050, height=500)
        self.frame.pack()

    def botoes(self):
        self.voltar = CTkButton(self.janela, text="Voltar", font=("Arial", 24, "bold"), width=150, corner_radius=32, hover_color="black", command=self.Voltar)
        self.voltar.place(x=70, y=660)

    def Voltar(self):
        self.janela.destroy()
        TelaPrincipal.TelaPrincipal()

    def treeview(self):
        self.scrollbary = Scrollbar(self.frame, orient=VERTICAL)

        self.tree = ttk.Treeview(self.frame, columns=("Tipo", "Modelo", "Marca", "Alugado", "Ano", "Placa", "KM Rodados", "Diária"),
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
        self.tree.column('#1', stretch=NO, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#2', stretch=NO, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#3', stretch=NO, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100, anchor=CENTER)
        self.tree.column('#5', stretch=NO, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#6', stretch=NO, minwidth=0, width=200, anchor=CENTER)
        self.tree.column('#7', stretch=NO, minwidth=0, width=150, anchor=CENTER)
        self.tree.column('#8', stretch=NO, minwidth=0, width=150, anchor=CENTER)

        self.tree.pack()

    def listar_veiculos(self):
        self.tree.delete(*self.tree.get_children())
        db.conecta_bd()
        db.cursor.execute("SELECT * FROM Veiculos ORDER BY Código ASC")
        self.lista = db.cursor.fetchall()

        for data in self.lista:
            self.tree.insert('', 'end', values=(data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]))


if __name__ == "__main__":
    TelaListarVeiculos()