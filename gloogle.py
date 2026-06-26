import tkinter as tk
from tkinter import ttk


class SearchApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # =========================
        # CONFIGURAÇÕES DA JANELA
        # =========================
        self.title("Barbie Search")
        self.geometry("900x650")
        self.configure(bg="#FFD6EC")
        self.minsize(400, 300)

        # =========================
        # CORES TEMA BARBIE
        # =========================
        self.bg_color = "#FFD6EC"        # Rosa claro
        self.card_color = "#FFF0F7"      # Branco rosado
        self.primary_pink = "#FF4FA3"    # Rosa Barbie
        self.dark_pink = "#E91E63"
        self.light_pink = "#FFC1DD"
        self.text_color = "#7A1E48"

        # =========================
        # CONTAINER CENTRAL
        # =========================
        main_frame = tk.Frame(
            self,
            bg=self.bg_color
        )

        main_frame.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # =========================
        # TÍTULO
        # =========================
        title_frame = tk.Frame(
            main_frame,
            bg=self.bg_color
        )

        title_frame.pack(pady=(0, 35))

        title = tk.Label(
            title_frame,
            text="Barbie Search",
            font=("Comic Sans MS", 42, "bold"),
            fg=self.primary_pink,
            bg=self.bg_color
        )

        title.pack()

        subtitle = tk.Label(
            title_frame,
            text="✨ Pesquise com estilo ✨",
            font=("Segoe UI", 14, "italic"),
            fg=self.dark_pink,
            bg=self.bg_color
        )

        subtitle.pack(pady=(5, 0))

        # =========================
        # CARD PESQUISA
        # =========================
        search_frame = tk.Frame(
            main_frame,
            bg=self.card_color,
            bd=0,
            highlightbackground=self.primary_pink,
            highlightthickness=3
        )

        search_frame.pack(
            ipadx=12,
            ipady=8,
            fill="x"
        )

        # =========================
        # ÍCONE LUPA
        # =========================
        search_icon = tk.Label(
            search_frame,
            text="💖",
            bg=self.card_color,
            font=("Segoe UI Emoji", 18)
        )

        search_icon.pack(
            side="left",
            padx=(15, 8)
        )

        # =========================
        # ENTRADA
        # =========================
        self.placeholder_text = "Digite sua pesquisa..."

        self.search_var = tk.StringVar()

        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Segoe UI", 15, "bold"),
            width=45,
            bd=0,
            bg=self.card_color,
            fg="gray",
            insertbackground=self.primary_pink,
            highlightthickness=0
        )

        self.search_entry.pack(
            side="left",
            padx=5,
            pady=8
        )

        self.search_entry.insert(0, self.placeholder_text)

        # =========================
        # MICROFONE
        # =========================
        mic_icon = tk.Label(
            search_frame,
            text="🎀",
            bg=self.card_color,
            font=("Segoe UI Emoji", 18)
        )

        mic_icon.pack(
            side="right",
            padx=(5, 15)
        )

        # =========================
        # EVENTOS
        # =========================
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_focus_out)
        self.search_entry.bind("<Return>", self.perform_search)

        # =========================
        # BOTÕES
        # =========================
        buttons_frame = tk.Frame(
            main_frame,
            bg=self.bg_color
        )

        buttons_frame.pack(pady=30)

        # Hover botão
        def hover_in(btn):
            btn.config(bg=self.dark_pink)

        def hover_out(btn):
            btn.config(bg=self.primary_pink)

        # =========================
        # BOTÃO PESQUISAR
        # =========================
        search_button = tk.Button(
            buttons_frame,
            text="Pesquisar",
            font=("Segoe UI", 12, "bold"),
            bg=self.primary_pink,
            fg="white",
            relief="flat",
            activebackground=self.dark_pink,
            activeforeground="white",
            padx=22,
            pady=10,
            cursor="hand2",
            command=self.perform_search
        )

        search_button.pack(
            side="left",
            padx=12
        )

        search_button.bind(
            "<Enter>",
            lambda e: hover_in(search_button)
        )

        search_button.bind(
            "<Leave>",
            lambda e: hover_out(search_button)
        )

        # =========================
        # BOTÃO SORTE
        # =========================
        feeling_lucky_button = tk.Button(
            buttons_frame,
            text="Estou com sorte",
            font=("Segoe UI", 12, "bold"),
            bg=self.primary_pink,
            fg="white",
            relief="flat",
            activebackground=self.dark_pink,
            activeforeground="white",
            padx=22,
            pady=10,
            cursor="hand2"
        )

        feeling_lucky_button.pack(
            side="left",
            padx=12
        )

        feeling_lucky_button.bind(
            "<Enter>",
            lambda e: hover_in(feeling_lucky_button)
        )

        feeling_lucky_button.bind(
            "<Leave>",
            lambda e: hover_out(feeling_lucky_button)
        )

        # =========================
        # RODAPÉ
        # =========================
        footer = tk.Label(
            self,
            text="Barbie Interface 💕",
            font=("Segoe UI", 10, "italic"),
            bg=self.bg_color,
            fg=self.dark_pink
        )

        footer.pack(side="bottom", pady=15)

    # =========================
    # PLACEHOLDER
    # =========================
    def on_entry_click(self, event):

        if self.search_entry.get() == self.placeholder_text:
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(
                fg=self.text_color
            )

    def on_focus_out(self, event):

        if self.search_entry.get() == "":
            self.search_entry.insert(0, self.placeholder_text)
            self.search_entry.config(
                fg="gray"
            )

    # =========================
    # PESQUISA
    # =========================
    def perform_search(self, event=None):

        query = self.search_entry.get()

        if query and query != self.placeholder_text:
            print(f"Pesquisando por: {query}")


# =========================
# EXECUÇÃO
# =========================
if __name__ == "__main__":
    app = SearchApp()
    app.mainloop()