import sqlite3


class DataBase_Clientes:
    def __init__(self):
        self.conecta_bd()
        self.montar_tabelas()

    def conecta_bd(self):
        self.conn = sqlite3.connect("DataBase.bd")
        self.cursor = self.conn.cursor()

    def montar_tabelas(self):
        self.conecta_bd()
        self.cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Clientes (
                        Código INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                        Nome TEXT NOT NULL,
                        CPF TEXT NOT NULL,
                        CNH TEXT NOT NULL,
                        Email TEXT NOT NULL,
                        Telefone TEXT NOT NULL,
                        CEP TEXT NOT NULL
                    );
                    """)

class DataBase_Veiculos:
    def __init__(self):
        self.conecta_bd()
        self.montar_tabelas()

    def conecta_bd(self):
        self.conn = sqlite3.connect("DataBase.bd")
        self.cursor = self.conn.cursor()

    def montar_tabelas(self):
        self.conecta_bd()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Veiculos (
                            Código INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            Tipo TEXT NOT NULL,
                            Modelo TEXT NOT NULL,
                            Marca TEXT NOT NULL,
                            Alugado TEXT NOT NULL,
                            Ano TEXT NOT NULL,
                            Placa TEXT NOT NULL,
                            Km TEXT NOT NULL,
                            Diaria REAL NOT NULL
                            );
                            """)


class DataBase_Alugueis:
    def __init__(self):
        self.conecta_bd()
        self.montar_tabelas()

    def conecta_bd(self):
        global cursor, conn
        self.conn = sqlite3.connect("DataBase.bd")
        self.cursor = self.conn.cursor()

    def montar_tabelas(self):
        global conn, cursor
        self.conecta_bd()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS Alugueis (
                                Código INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                Modelo TEXT NOT NULL,
                                Placa TEXT NOT NULL,
                                DataLocação TEXT NOT NULL,
                                DataDevolução TEXT NOT NULL,
                                Valor REAL NOT NULL
                                );
                                """)