import tkinter as tk

class MenuPrincipal:
    def __init__(self, master, app):
        """Tela de Menu Principal"""
        self.master = master
        self.app = app
        self.frame = tk.Frame(master)
        self.frame.pack()

        # Título do Menu
        tk.Label(self.frame, text="Menu Principal", font=("Arial", 20)).pack(pady=20)

        # Botões
        tk.Button(self.frame, text="Cadastrar Pessoa", font=("Arial", 14), width=20, 
                  command=self.app.abrir_tela_cadastro).pack(pady=10)
        tk.Button(self.frame, text="Visualizar Registros", font=("Arial", 14), width=20, 
                  command=self.app.abrir_tela_Registados).pack(pady=10)
        tk.Button(self.frame, text="Sair", font=("Arial", 14), width=20, 
                  command=self.master.quit).pack(pady=10)

    def destruir(self):
        """Remove os widgets da tela"""
        self.frame.destroy()


class App:
    def __init__(self, root):
        self.root = root
        self.tela_atual = None
        self.abrir_menu_principal()
    
    def abrir_menu_principal(self):
        if self.tela_atual:
            self.tela_atual.destruir()
        self.atual = MenuPrincipal(self.root, self)
    
    def abrir_tela_cadastro(self):
        print("tela Aberta")

    def abrir_tela_Registados(self):
        print("tela aberta")


if __name__ == "__main__":
   root = tk.Tk()
   root.title("Sistema do Dizimo")
   root.geometry("800x600")
   root.resizable(False,False)

   app = App(root)
   root.mainloop()





