import tkinter as tk
from tkinter import messagebox
import re 

class SistemadeCasdastro:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Cadastro")
        
        self.cadastro = []

        tk.Label(self.master, text="Nome", font=("Arial", 20), fg="blue").grid(row=0, column=0, columnspan=2)
        tk.Label(self.master, text="Conjuge", font=("Arial", 20), fg="blue").grid(row=1, column=0, columnspan=2)
        tk.Label(self.master, text="Data de Nascimento", font=("Arial", 20), fg="blue").grid(row=2, column=0, columnspan=2)        
        tk.Label(self.master, text="Telefone", font=("Arial", 20), fg="blue").grid(row=4, column=0, columnspan=2)
        tk.Label(self.master, text="Endereço", font=("Arial", 20), fg="blue").grid(row=5, column=0, columnspan=2)
        tk.Label(self.master, text="Data de Casamento", font=("Arial", 20), fg="blue").grid(row=6, column=0, columnspan=2)
        tk.Label(self.master, text="Cadastro", font=("Arial", 20), fg="blue").grid(row=7, column=0, columnspan=2)
        tk.Label(self.master, text="Primeira contribuição", font=("Arial", 20), fg="blue").grid(row=8, column=0, columnspan=2)
        
        self.nome = tk.Entry(self.master)
        self.nome.grid(row=0, column=1)

        self.conjuge = tk.Entry(self.master)
        self.conjuge.grid(row=1, column=1)

        self.data_nascimento = tk.Entry(self.master)
        self.data_nascimento.grid(row=2, column=1)

        self.telefone = tk.Entry(self.master)
        self.telefone.grid(row=4, column=1)

        self.endereco = tk.Entry(self.master)
        self.endereco.grid(row=5, column=1)

        self.data_casamento = tk.Entry(self.master)
        self.data_casamento.grid(row=6, column=1)

        self.cadastro = tk.Entry(self.master)
        self.cadastro.grid(row=7, column=1)

        self.primeira_contribuicao = tk.Entry(self.master)
        self.primeira_contribuicao.grid(row=8, column=1)        

        tk.button(self.master, text="Adicionar", command=self.adicionar_dados).grid(row=10, column=1)
        tk.Button(self.master, text="Excluir", command=self.excluir_dados).grid(row=10, column=2)
        tk.Button(self.master, text="Sair", command=self.sair).grid(row=10, column=2)


        def validar_email(email):
            if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
                return True
            else:
                return False
            
        def validar_telefone(telefone):
            if re.match(r"^\d{10}$", telefone):
                return True
            else:
                return False
            
        def validar_data(data):
            if re.match(r"^\d{2}/\d{2}/\d{4}$", data):
                return True
            else:
                return False
            
        def cadastrar(self):
            nome =  self.nome.entry.get().stip()
            conjuge = self.conjuge.entry.get().strip()
            data_nascimento = self.data_nascimento.entry.get().strip()
            telefone = self.telefone.entry.get().strip()
            endereco = self.endereco.entry.get().strip()
            data_casamento = self.data_casamento.entry.get().strip()
            cadastro = self.cadastro.entry.get().strip()
            primeira_contribuicao = self.primeira_contribuicao.entry.get().strip()
            
            self.cadastro.append([nome, conjuge, data_nascimento, telefone, endereco, data_casamento, cadastro, primeira_contribuicao])
            self.cadastro.sort(key=lambda x: x[0])
            messagebox.showinfo("Cadastro", "Cadastro adicionado com sucesso!")              

    def selecionar(self, event):
        self.selecionado = self.cadastro.selection()
        if self.selecionado:
            self.nome.delete(0, tk.END)
            self.nome.insert(0, self.selecionado[0])
            self.conjuge.delete(0, tk.END)
            self.conjuge.insert(0, self.selecionado[1])
            self.data_nascimento.delete(0, tk.END)
            self.data_nascimento.insert(0, self.selecionado[2])
            self.telefone.delete(0, tk.END)
            self.telefone.insert(0, self.selecionado[3])
            self.endereco.delete(0, tk.END)
            self.endereco.insert(0, self.selecionado[4])
            self.data_casamento.delete(0, tk.END)
            self.data_casamento.insert(0, self.selecionado[5])
            self.cadastro.delete(0, tk.END)
            self.cadastro.insert(0, self.selecionado[6])
            self.primeira_contribuicao.delete(0, tk.END)
            self.primeira_contribuicao.insert(0, self.selecionado[7])

        self.salvar.configure(state=tk.NORMAL)
        self.excluir.configure(state=tk.NORMAL)

    def editar(self, event):
        self.selecionado = self.cadastro.selection()
        if self.selecionado:
            self.nome.delete(0, tk.END)
            self.nome.insert(0, self.selecionado[0])
            self.conjuge.delete(0, tk.END)
            self.conjuge.insert(0, self.selecionado[1])
            self.data_nascimento.delete(0, tk.END)
            self.data_nascimento.insert(0, self.selecionado[2])
            self.telefone.delete(0, tk.END)
            self.telefone.insert(0, self.selecionado[3])
            self.endereco.delete(0, tk.END)
            self.endereco.insert(0, self.selecionado[4])
            self.data_casamento.delete(0, tk.END)
            self.data_casamento.insert(0, self.selecionado[5])
            self.cadastro.delete(0, tk.END)
            self.cadastro.insert(0, self.selecionado[6])
            self.primeira_contribuicao.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SistemadeCasdastro(root)
    root.mainloop()