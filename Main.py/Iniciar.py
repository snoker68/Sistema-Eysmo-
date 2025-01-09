import tkinter as tk
import Cadastro

class MenuPrincipal:
    def __init__(self, master):
        """Tela de Menu Principal"""
        self.master = master
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Título do Menu
        tk.Label(self.frame, text="Menu Principal", font=("Arial", 20)).pack(pady=20)

        # Botões
        tk.Button(self.frame, text="Cadastro de Dizimista", font=("Arial", 14), width=20, 
                  command=self.cadastrar_dizimista).pack(pady=10)
        tk.Button(self.frame, text="Visualizar Pagamento", font=("Arial", 14), width=20, 
                  command=self.visualizar_pagamento).pack(pady=10)
        tk.Button(self.frame, text="Efetuar Pagamento", font=("Arial", 14), width=20, 
                  command=self.efetuar_pagamento).pack(pady=10)
        tk.Button(self.frame, text="Sair", font=("Arial", 14), width=20, 
                  command=self.master.quit).pack(pady=10)

    def cadastrar_dizimista(self):        
        cadastro = Cadastro.Cadastro()
        tela_cadastro = Cadastro.TelaCadastro(self.master, cadastro)
        self.destruir()

    def visualizar_pagamento(self):
        print("Visualizar Pagamento clicado!")

    def efetuar_pagamento(self):
        print("Efetuar Pagamento clicado!")

    def destruir(self):
        """Remove os widgets da tela"""
        self.frame.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Menu Principal")
    root.geometry("600x500")
    root.resizable(False, False)

    menu = MenuPrincipal(root)
    root.mainloop()
