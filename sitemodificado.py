import tkinter as tk
from tkinter import ttk, messagebox


class AppRealityShow(tk.Tk):
    def __init__(self):
        super().__init__()

        # =========================
        # CONFIGURAÇÃO DA JANELA
        # =========================
        self.title("Reality Show - Seleção Oficial")
        self.geometry("950x700")
        self.configure(bg="#12071F")
        self.resizable(False, False)

        # =========================
        # PALETA DE CORES
        # =========================
        self.bg_color = "#12071F"
        self.card_color = "#1D102E"

        self.accent_color = "#FF2E93"
        self.hover_color = "#FF5CAD"

        self.input_bg = "#2A173F"
        self.border_color = "#5A2D82"

        self.text_main = "#FFFFFF"
        self.text_secondary = "#C9A9E9"

        self.success_color = "#00FFB3"

        # =========================
        # ESTILO COMBOBOX
        # =========================
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Custom.TCombobox",
            fieldbackground=self.input_bg,
            background=self.card_color,
            foreground=self.text_main,
            bordercolor=self.border_color,
            arrowcolor=self.accent_color,
            padding=8
        )

        self.create_widgets()

    def create_widgets(self):

        # =========================
        # CABEÇALHO
        # =========================
        header = tk.Frame(
            self,
            bg=self.bg_color
        )

        header.pack(fill="x", pady=(40, 20))

        title_small = tk.Label(
            header,
            text="🎬 SELEÇÃO OFICIAL 2026 🎬",
            font=("Segoe UI", 12, "bold"),
            bg=self.bg_color,
            fg=self.accent_color
        )

        title_small.pack()

        title = tk.Label(
            header,
            text="Reality Show",
            font=("Montserrat", 36, "bold"),
            bg=self.bg_color,
            fg=self.text_main
        )

        title.pack(pady=(5, 0))

        subtitle = tk.Label(
            header,
            text="Cadastro de Participantes",
            font=("Segoe UI", 16),
            bg=self.bg_color,
            fg=self.text_secondary
        )

        subtitle.pack()

        line = tk.Frame(
            header,
            bg=self.accent_color,
            width=180,
            height=3
        )

        line.pack(pady=15)

        # =========================
        # CARD
        # =========================
        card = tk.Frame(
            self,
            bg=self.card_color,
            highlightbackground=self.border_color,
            highlightthickness=2
        )

        card.pack(
            padx=90,
            pady=20,
            fill="both",
            expand=True
        )

        form_frame = tk.Frame(
            card,
            bg=self.card_color
        )

        form_frame.pack(
            padx=35,
            pady=30,
            fill="both",
            expand=True
        )

        # =========================
        # FUNÇÃO INPUT
        # =========================
        def create_input(parent, label_text, row, col, width=30):

            lbl = tk.Label(
                parent,
                text=label_text,
                font=("Segoe UI", 10, "bold"),
                bg=self.card_color,
                fg=self.text_secondary
            )

            lbl.grid(
                row=row,
                column=col,
                sticky="w",
                pady=(12, 4),
                padx=15
            )

            entry = tk.Entry(
                parent,
                font=("Segoe UI", 13),
                bg=self.input_bg,
                fg=self.text_main,
                insertbackground=self.accent_color,
                relief="flat",
                width=width,
                highlightthickness=2,
                highlightbackground=self.border_color,
                highlightcolor=self.accent_color
            )

            entry.grid(
                row=row + 1,
                column=col,
                sticky="we",
                padx=15,
                pady=(0, 10),
                ipady=10
            )

            return entry

        # =========================
        # CAMPOS
        # =========================
        self.ent_nome = create_input(
            form_frame,
            "NOME ARTÍSTICO",
            0,
            0,
            35
        )

        self.ent_idade = create_input(
            form_frame,
            "IDADE",
            0,
            1,
            20
        )

        self.ent_instagram = create_input(
            form_frame,
            "INSTAGRAM",
            2,
            0,
            35
        )

        self.ent_cidade = create_input(
            form_frame,
            "CIDADE",
            2,
            1,
            25
        )

        # =========================
        # COMBOBOX PERFIL
        # =========================
        lbl_tipo = tk.Label(
            form_frame,
            text="PERFIL DO PARTICIPANTE",
            font=("Segoe UI", 10, "bold"),
            bg=self.card_color,
            fg=self.text_secondary
        )

        lbl_tipo.grid(
            row=4,
            column=0,
            sticky="w",
            pady=(12, 4),
            padx=15
        )

        self.combo_tipo = ttk.Combobox(
            form_frame,
            values=[
                "Influencer",
                "Atleta",
                "Cantor(a)",
                "Streamer",
                "Modelo",
                "Anônimo"
            ],
            font=("Segoe UI", 12),
            state="readonly",
            style="Custom.TCombobox"
        )

        self.combo_tipo.grid(
            row=5,
            column=0,
            sticky="we",
            padx=15,
            pady=(0, 10)
        )

        self.combo_tipo.set("Influencer")

        # =========================
        # DROPDOWN
        # =========================
        self.option_add(
            '*TCombobox*Listbox.background',
            self.input_bg
        )

        self.option_add(
            '*TCombobox*Listbox.foreground',
            self.text_main
        )

        self.option_add(
            '*TCombobox*Listbox.selectBackground',
            self.accent_color
        )

        self.option_add(
            '*TCombobox*Listbox.selectForeground',
            "#FFFFFF"
        )

        self.option_add(
            '*TCombobox*Listbox.font',
            ("Segoe UI", 12)
        )

        # GRID
        form_frame.columnconfigure(0, weight=1)
        form_frame.columnconfigure(1, weight=1)

        # =========================
        # BOTÃO
        # =========================
        btn_frame = tk.Frame(
            self,
            bg=self.bg_color
        )

        btn_frame.pack(pady=(10, 35))

        self.btn_cadastrar = tk.Button(
            btn_frame,
            text="ENVIAR INSCRIÇÃO",
            font=("Segoe UI", 13, "bold"),
            bg=self.accent_color,
            fg="white",
            activebackground=self.hover_color,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            padx=40,
            pady=14,
            command=self.cadastrar
        )

        self.btn_cadastrar.pack()

        # Hover
        self.btn_cadastrar.bind(
            "<Enter>",
            lambda e: self.btn_cadastrar.config(bg=self.hover_color)
        )

        self.btn_cadastrar.bind(
            "<Leave>",
            lambda e: self.btn_cadastrar.config(bg=self.accent_color)
        )

        # =========================
        # STATUS
        # =========================
        self.status_lbl = tk.Label(
            self,
            text="",
            font=("Segoe UI", 11),
            bg=self.bg_color,
            fg=self.success_color
        )

        self.status_lbl.pack(pady=10)

    # =========================
    # CADASTRAR
    # =========================
    def cadastrar(self):

        nome = self.ent_nome.get()
        idade = self.ent_idade.get()
        perfil = self.combo_tipo.get()

        if not nome or not idade:
            messagebox.showwarning(
                "Atenção",
                "Nome artístico e idade são obrigatórios!",
                parent=self
            )
            return

        self.status_lbl.config(
            text="Analisando perfil...",
            fg=self.text_main
        )

        self.update()
        self.after(700)

        self.status_lbl.config(
            text=f"✓ {nome} foi pré-selecionado(a) para o Reality Show!",
            fg=self.success_color
        )

        # LIMPAR CAMPOS
        self.ent_nome.delete(0, tk.END)
        self.ent_idade.delete(0, tk.END)
        self.ent_instagram.delete(0, tk.END)
        self.ent_cidade.delete(0, tk.END)

        self.combo_tipo.set("Influencer")

        self.ent_nome.focus()


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":
    app = AppRealityShow()
    app.mainloop()