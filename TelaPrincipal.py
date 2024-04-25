from customtkinter import *
from tkinter import PhotoImage
import TelaCadastroVeículos
import TelaCadastroClientes
import TelaListarClientes
import TelaListarVeiculos
import TelaListarAluguel


class TelaPrincipal:
    def __init__(self):
        self.janela = CTk()
        self.tema()
        self.tela()
        self.Frames()
        self.Imagem()
        self.Labels()
        self.Botoes()

        self.janela.mainloop()

    def tema(self):
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

    def tela(self):
        self.janela.title("Sistema de Aluguel de Veículos")
        self.janela.geometry("1280x720")
        self.janela.resizable(False,False)

    def Frames(self):
        self.frame = CTkFrame(self.janela, width=640, height=720)
        self.frame.pack(side=RIGHT)

    def Imagem(self):
        self.car_img = PhotoImage(file="Imagens/background.png")
        self.car_imgLabel = CTkLabel(self.janela, image= self.car_img, text=None)
        self.car_imgLabel.place(x=0, y=0)

    def Botoes(self):
        self.botao_fonte = ("Arial", 24)

        self.alugarV = CTkButton(self.frame, text="Alugar Veículos", width=300, height=75, font=self.botao_fonte, corner_radius=32, bg_color="white", hover_color="black", command=self.CadastroClientes)
        self.alugarV.place(x=170, y=120)

        self.veiculoCad = CTkButton(self.frame, text="Cadastrar Veículos", width=300, height=75, font=self.botao_fonte, corner_radius=32, bg_color="white", hover_color="black", command=self.CadastroVeiculos)
        self.veiculoCad.place(x=170, y=220)

        self.listaC = CTkButton(self.frame, text="Lista de Clientes", width=300, height=75, font=self.botao_fonte, corner_radius=32, bg_color="white", hover_color="black", command=self.ListarClientes)
        self.listaC.place(x=170, y=320)

        self.listaV = CTkButton(self.frame, text="Lista de Veículos", width=300, height=75, font=self.botao_fonte, corner_radius=32, bg_color="white", hover_color="black", command=self.ListarVeiculos)
        self.listaV.place(x=170, y=420)

        self.listaA = CTkButton(self.frame, text="Lista de Aluguéis", width=300, height=75, font=self.botao_fonte,corner_radius=32, bg_color="white", hover_color="black", command=self.ListarAlugueis)
        self.listaA.place(x=170, y=520)

    def Labels(self):
        self.fundo = CTkLabel(self.frame, text="", width=350, height=500, corner_radius=32, fg_color="white")
        self.fundo.place(relx=0.5, rely=0.5, anchor="center")

    def CadastroVeiculos(self):
        self.janela.destroy()
        TelaCadastroVeículos.TelaCadastroVeiculos()

    def CadastroClientes(self):
        self.janela.destroy()
        TelaCadastroClientes.TelaCadastroClientes()

    def ListarClientes(self):
        self.janela.destroy()
        TelaListarClientes.TelaListarClientes()

    def ListarVeiculos(self):
        self.janela.destroy()
        TelaListarVeiculos.TelaListarVeiculos()

    def ListarAlugueis(self):
        self.janela.destroy()
        TelaListarAluguel.TelaListarAluguel()


if __name__ == "__main__":
     TelaPrincipal()