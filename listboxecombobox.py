import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Função para cadastrar aluno
def cadastrar():
    nome = entry_nome.get()
    curso = combo_curso.get()

    if nome == "":
        messagebox.showwarning("Aviso", "Digite o nome do aluno!")
        return

    aluno = f"{nome} - {curso}"
    listbox.insert(tk.END, aluno)

    entry_nome.delete(0, tk.END)
    combo_curso.current(0)

# Função para remover aluno
def remover():
    try:
        indice = listbox.curselection()[0]
        listbox.delete(indice)
    except:
        messagebox.showwarning("Aviso", "Selecione um aluno!")

# Função para limpar campos
def limpar():
    entry_nome.delete(0, tk.END)
    combo_curso.current(0)

# Janela principal
janela = tk.Tk()
janela.title("Cadastro de Alunos")
janela.geometry("450x400")
janela.resizable(False, False)

# Título
titulo = tk.Label(
    janela,
    text="Cadastro de Alunos",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

# Nome
tk.Label(janela, text="Nome do aluno").pack()

entry_nome = tk.Entry(janela, width=40)
entry_nome.pack(pady=5)

# Curso
tk.Label(janela, text="Curso").pack()

combo_curso = ttk.Combobox(
    janela,
    values=[
        "Informática",
        "Administração",
        "Enfermagem",
        "Agronomia",
        "Direito"
    ],
    state="readonly",
    width=37
)

combo_curso.current(0)
combo_curso.pack(pady=5)

# Botões
frame = tk.Frame(janela)
frame.pack(pady=10)

tk.Button(
    frame,
    text="Cadastrar",
    width=12,
    command=cadastrar,
    bg="green",
    fg="white"
).grid(row=0, column=0, padx=5)

tk.Button(
    frame,
    text="Remover",
    width=12,
    command=remover,
    bg="red",
    fg="white"
).grid(row=0, column=1, padx=5)

tk.Button(
    frame,
    text="Limpar",
    width=12,
    command=limpar,
    bg="gray",
    fg="white"
).grid(row=0, column=2, padx=5)

# Lista de alunos
tk.Label(janela, text="Alunos cadastrados").pack()

listbox = tk.Listbox(
    janela,
    width=50,
    height=10,
    font=("Arial", 10)
)

listbox.pack(pady=10)

janela.mainloop()