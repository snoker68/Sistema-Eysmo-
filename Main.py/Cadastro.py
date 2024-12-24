import tkinter as tk
from tkinter import messagebox
from datetime import datetime

Class TelaCadastro:
    def __init__(self, master):
        self.master = master
        self.app = app
        self.frame = tk.Frame(master)
        self.frame.pack()

        tk.Label(self.frame, text= "Cadastrar Dizimista", font=("Arial", 14), width=15, command=self.cadatrar).grid(row=0, column=0, pady=10, padx= 10)

        tk.Label(self.frame, text= "editar", font=("Arial", 14), width=15, command=self.editar).grid(row  = 0, column = 1, pady = 10, padx = 10)

        self.lista.frame = tk.Frame(self.frame)
        self.lista.frame.grid(row = 1, column = 0, pady = 2, padx = 10)
        self.atualizar_lista()

        self.campos_frame = tk.Frame(self.frame)
        self.campos_frame.grid(row = 1, column = 1, pady = 2, padx = 10)
        self.atualizar_campos()

        tk.label(self.campos_frame, text="Nome Completo", font=("Arial", 12)).grid(row = 0, column = 0, pady = 2, padx = 10)
        tk.label(self.campos_frame, text="Data Nascimento", font=("Arial", 12)).grid(row = 1, column = 0, pady = 2, padx = 10)        
        tk.label(self.campos_frame, text="Telefone", font=("Arial", 12)).grid(row = 3, column = 0, pady = 2, padx = 10)
        tk.label(self.campos_frame, text="Endereço", font=("Arial", 12)).grid(row = 4, column = 0, pady = 2, padx = 10)
        tk.nome_completo = tk.Entry(self.campos_frame)
        tk.nome_completo.grid(row = 0, column = 1, pady = 2, padx = 10)
        tk.data_nascimento = tk.Entry(self.campos_frame)
        tk.data_nascimento.grid(row = 1, column = 1, pady = 2, padx = 10)
        tk.telefone = tk.Entry(self.campos_frame)
        tk.telefone.grid(row = 3, column = 1, pady = 2, padx = 10)
        tk.endereco = tk.Entry(self.campos_frame)
        tk.endereco.grid(row = 4, column = 1, pady = 2, padx = 10)

        tk.Button(self.campos_frame, text="Salvar", command=self.Salvar_cadastro).grid(row = 5, column = 0, pady = 2, padx = 10)

    def mostrar_campos(self):
        self.campos_frame.grid()

    def salvar_cadastro(self):
        self.nome_completo = tk.nome_completo.get()
        self.data_nascimento = tk.data_nascimento.get()
        self.telefone = tk.telefone.get()
        self.endereco = tk.endereco.get()
        self.atualizar_lista()

        if nome_completo == "" or data_nascimento == "" or telefone == "" or endereco == "":
            data_cadastro = datetime.now().strftime("%d/%m/%Y")
            self.app.cadastro.adicionar_registro(self.nome_completo, self.data_nascimento, self.telefone, self.endereco, data_cadastro)

            self.atualizar_lista()
            self.nome_entry.delete(0, tk.END)
            self.campos_frame.grid_remove()
            messagebox.showinfo("Sucesso", "Cadastro efetuado com sucesso!")
        else:
            messagebox.showinfo("Erro", "Preencha todos os campos!")

    def editar_registro(self, nome_completo, data_nascimento, telefone, endereco):
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.endereco = endereco

        self.atualizar_campos()
        self.campos_frame.grid()

    def atualizar_lista(self):
        self.lista.atualizar()

    def atualizar_campos(self):
        self.nome_entry = tk.Entry(self.campos_frame)
        self.nome_entry.grid(row = 0, column = 1, pady = 2, padx = 10)
        self.nome_entry.insert(0, self.nome_completo)
        self.data_entry = tk.Entry(self.campos_frame)
        self.data_entry.grid(row = 1, column = 1, pady = 2, padx = 10)
        self.data_entry.insert(0, self.data_nascimento)
        self.telefone_entry = tk.Entry(self.campos_frame)
        self.telefone_entry.grid(row = 3, column = 1, pady = 2, padx = 10)
        self.telefone_entry.insert(0, self.telefone)
        self.endereco_entry = tk.Entry(self.campos_frame)
        self.endereco_entry.grid(row = 4, column = 1, pady = 2, padx = 10)
        self.endereco_entry.insert(0, self.endereco)

    def Salvar_cadastro(self):
        self.nome = self.nome_entry.get()
        self.data_nascimento = self.data_entry.get()
        self.telefone = self.telefone_entry.get()
        self.endereco = self.endereco_entry.get()
        self.salvar_cadastro()
    
class cadastro:
    def __init__(self):
        self.registro = []
    
    def adicionar_registro(self, nome, data_nascimento, telefone, endereco):
        registro = {nome, data_nascimento, telefone, endereco}
        self.registro.insert(0, registro)
    
    def obter_registro(self):
        return self.registro

class App:
    def __init__(self):
        self.root = root
        self.cadastro = cadastro()
        self.tela_cadastro = tela_cadastro(self.root, self.cadastro)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Cadastro")
    root.geometry("600x500")
    root.resizable(False, False)

    app = App(root)
    root.mainloop()
    


