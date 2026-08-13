import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Conversor de Moedas")

janela_largura = 400
janela_altura = 250

tela_largura = root.winfo_screenwidth()
tela_altura = root.winfo_screenheight()

centro_x = int(tela_largura / 2 - janela_largura / 2)
centro_y = int(tela_altura / 2 - janela_altura / 2)

root.geometry(
    f"{janela_largura}x{janela_altura}+{centro_x}+{centro_y}"
)

# VALOR

text = tk.Label(
    root,
    text="Valor:",
    font=("Arial", 12)
)
text.grid(
    row=0,
    column=0,
    pady=5,
    padx=5,
    sticky="w"
)

valor_entry = tk.Entry(
    root,
    font=("Arial", 12)
)
valor_entry.grid(
    row=0,
    column=1,
    pady=5,
    padx=5
)

# MOEDA DE ORIGEM

origem_label = tk.Label(
    root,
    text="Moeda de origem:",
    font=("Arial", 12)
)
origem_label.grid(
    row=1,
    column=0,
    pady=5,
    padx=5,
    sticky="w"
)

origem = ttk.Combobox(
    root,
    values=["USD", "BRL", "EUR", "GBP", "JPY"],
    font=("Arial", 12),
    state="readonly"
)
origem.grid(
    row=1,
    column=1,
    pady=5,
    padx=5
)

origem.set("BRL")

# MOEDA DE DESTINO

destino_label = tk.Label(
    root,
    text="Moeda de destino:",
    font=("Arial", 12)
)
destino_label.grid(
    row=2,
    column=0,
    pady=5,
    padx=5,
    sticky="w"
)

destino = ttk.Combobox(
    root,
    values=["USD", "BRL", "EUR", "GBP", "JPY"],
    font=("Arial", 12),
    state="readonly"
)
destino.grid(
    row=2,
    column=1,
    pady=5,
    padx=5
)

destino.set("JPY")

# TAXAS DE CONVERSÃO

taxas = {
    "BRL": {
        "BRL": 1,
        "USD": 0.18,
        "EUR": 0.15,
        "GBP": 0.14,
        "JPY": 26.5
    },

    "USD": {
        "BRL": 5.50,
        "USD": 1,
        "EUR": 0.86,
        "GBP": 0.76,
        "JPY": 147.00
    },

    "EUR": {
        "BRL": 6.40,
        "USD": 1.16,
        "EUR": 1,
        "GBP": 0.88,
        "JPY": 171
    },

    "GBP": {
        "BRL": 7.25,
        "USD": 1.32,
        "EUR": 1.14,
        "GBP": 1,
        "JPY": 194
    },

    "JPY": {
        "BRL": 0.037,
        "USD": 0.0068,
        "EUR": 0.0058,
        "GBP": 0.0052,
        "JPY": 1
    }
}

# FUNÇÃO PARA CONVERTER

def converter():

    try:
        valor = float(valor_entry.get())

        moeda_origem = origem.get()
        moeda_destino = destino.get()

        taxa = taxas[moeda_origem][moeda_destino]

        resultado = valor * taxa

        calculo.config(
            text=f"{valor:.2f} {moeda_origem} = {resultado:.2f} {moeda_destino}"
        )

    except ValueError:

        messagebox.showerror(
            "Erro",
            "Digite um valor válido!"
        )


# BOTÃO

botao = tk.Button(
    root,
    text="Converter",
    font=("Arial", 12),
    command=converter,
    cursor="hand2"

)

botao.grid(
    row=4,
    column=0,
    columnspan=2,
    pady=10
)

# RESULTADO

resultado_label = tk.Label(
    root,
    text="Resultado:",
    font=("Arial", 12)
)

resultado_label.grid(
    row=5,
    column=0,
    pady=5,
    padx=5,
    sticky="w"
)

calculo = tk.Label(
    root,   
    text="--",
    font=("Arial", 12)
)

calculo.grid(
    row=5,
    column=1,
    pady=5,
    padx=5
)

# ATUALIZA O TEXTO AO TROCAR AS MOEDAS

def atualizar_resultado(event=None):

    moeda_origem = origem.get()
    moeda_destino = destino.get()

    calculo.config(
        text=f"-- {moeda_origem} = -- {moeda_destino}"
    )


origem.bind("<<ComboboxSelected>>", atualizar_resultado)
destino.bind("<<ComboboxSelected>>", atualizar_resultado)

root.mainloop()