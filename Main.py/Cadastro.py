import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import Iniciar

class TelaCadastro:
    def __init__(self, master, cadastro):
        self.master = master
        self.cadastro = cadastro
        self.frame = tk.Frame(master)
        self.frame.pack()

        #self.tela_cadastro = TelaCadastro(self.master, self.cadastro, self.menu_principal)

        # Botões principais
        tk.Button(self.frame, text="Cadastrar", font=("Arial", 14), command=self.mostrar_campos).grid(row=0, column=0, pady=10, padx=10)
        tk.Button(self.frame, text="Deletar", font=("Arial", 14), command=self.deletar_selecionado).grid(row=0, column=1, pady=10, padx=10)
        #tk.Button(self.frame, text="Editar", font=("Arial", 14), command=self.editar_selecionado).grid(row=0, column=2, pady=10, padx=10)
        #tk.Button(self.frame, text="Voltar Menu pricipal", font=("Arial", 14), command=self.voltar_menu).grid(row=0, column=2, pady=10, padx=10)

        # Listbox para exibir registros
        self.lista_frame = tk.Frame(self.frame)
        self.lista_frame.grid(row=1, column=0, columnspan=2, pady=2, padx=10)
        self.lista_box = tk.Listbox(self.lista_frame, font=("Arial", 12), width=50, height=15)
        self.lista_box.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)
        self.lista_box.bind("<Double-1>", self.mostrar_informacoes)

        # Barra de rolagem para o Listbox
        scrollbar = tk.Scrollbar(self.lista_frame, orient=tk.VERTICAL, command=self.lista_box.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista_box.config(yscrollcommand=scrollbar.set)

        # Campos de entrada para cadastro
        self.campos_frame = tk.Frame(self.frame)
        self.nome_completo = tk.Entry(self.campos_frame)
        self.data_nascimento = tk.Entry(self.campos_frame)
        self.telefone = tk.Entry(self.campos_frame)
        self.endereco = tk.Entry(self.campos_frame)

        self.atualizar_lista()

    def voltar_menu(self):
        Iniciar.MenuPrincipal(self.master)
        self.master.destroy()

    def atualizar_lista(self):
        """Atualiza a lista de registros exibidos."""
        self.lista_box.delete(0, tk.END)  # Limpa o Listbox
        registros = self.cadastro.obter_registros()
        for idx, registro in enumerate(registros):
            self.lista_box.insert(tk.END, f"{idx + 1}. {registro['nome']}")

    def mostrar_campos(self):
        """Exibe os campos de entrada para cadastro e esconde a lista."""
        self.lista_frame.grid_remove()  # Esconde o Listbox
        self.campos_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

        tk.Label(self.campos_frame, text="Nome Completo", font=("Arial", 12)).grid(row=0, column=0, pady=2, padx=10)
        tk.Label(self.campos_frame, text="Data Nascimento", font=("Arial", 12)).grid(row=1, column=0, pady=2, padx=10)
        tk.Label(self.campos_frame, text="Telefone", font=("Arial", 12)).grid(row=2, column=0, pady=2, padx=10)
        tk.Label(self.campos_frame, text="Endereço", font=("Arial", 12)).grid(row=3, column=0, pady=2, padx=10)

        self.nome_completo.grid(row=0, column=1, pady=2, padx=10)
        self.data_nascimento.grid(row=1, column=1, pady=2, padx=10)
        self.telefone.grid(row=2, column=1, pady=2, padx=10)
        self.endereco.grid(row=3, column=1, pady=2, padx=10)

        tk.Button(self.campos_frame, text="Salvar", command=self.salvar_cadastro).grid(row=4, column=0, columnspan=2, pady=10)

    def salvar_cadastro(self):
        """Salva um novo cadastro e exibe novamente a lista."""
        nome = self.nome_completo.get().strip()
        data_nascimento = self.data_nascimento.get().strip()
        telefone = self.telefone.get().strip()
        endereco = self.endereco.get().strip()

        if not all([nome, data_nascimento, telefone, endereco]):
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

        try:
            datetime.strptime(data_nascimento, "%d/%m/%Y")  # Validar data
        except ValueError:
            messagebox.showerror("Erro", "Data de nascimento inválida! Use o formato DD/MM/AAAA.")
            return

        self.cadastro.adicionar_registro(nome, data_nascimento, telefone, endereco)
        self.atualizar_lista()

        self.nome_completo.delete(0, tk.END)
        self.data_nascimento.delete(0, tk.END)
        self.telefone.delete(0, tk.END)
        self.endereco.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Cadastro efetuado com sucesso!")

        self.campos_frame.grid_remove()  # Esconde os campos de entrada
        self.lista_frame.grid(row=1, column=0, columnspan=2, pady=2, padx=10)  # Mostra novamente a lista

    def deletar_selecionado(self):
        """Deleta o registro selecionado no Listbox."""
        selecionado = self.lista_box.curselection()
        if not selecionado:
            messagebox.showerror("Erro", "Selecione um registro para deletar!")
            return

        indice = selecionado[0]  # Pega o índice selecionado
        self.cadastro.deletar_registro(indice)
        self.atualizar_lista()
        messagebox.showinfo("Sucesso", "Registro deletado com sucesso!")

    def mostrar_informacoes(self, event):
        """Exibe informações completas do registro selecionado."""
        selecionado = self.lista_box.curselection()
        if not selecionado:
            return

        indice = selecionado[0]
        registro = self.cadastro.obter_registros()[indice]

        info_window = tk.Toplevel(self.master)
        info_window.title("Informações do Registro")
        info_window.geometry("300x200")

        for chave, valor in registro.items():
            tk.Label(info_window, text=f"{chave.capitalize()}: {valor}", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)

class Cadastro:
    def __init__(self):
        self.registros = []

    def adicionar_registro(self, nome, data_nascimento, telefone, endereco):
        registro = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "telefone": telefone,
            "endereco": endereco
        }
        self.registros.append(registro)

    def obter_registros(self):
        return self.registros

    def deletar_registro(self, indice):
        if 0 <= indice < len(self.registros):
            del self.registros[indice]

class App:
    def __init__(self, root):
        self.root = root
        self.cadastro = Cadastro()
        self.tela_cadastro = TelaCadastro(self.root, self.cadastro)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Cadastro")
    root.geometry("600x500")
    root.resizable(False, False)

    app = App(root)
    root.mainloop()
