
import tkinter as tk
from tkinter import messagebox


# ============================================================
# JANELA PRINCIPAL
# ============================================================

root = tk.Tk()

root.title("Desenvolvimento de Sistemas - Janela Básica")
root.configure(bg="black")


# ============================================================
# TAMANHO E POSIÇÃO DA JANELA
# ============================================================

janela_largura = 300
janela_altura = 600

# Descobre o tamanho da tela
tela_largura = root.winfo_screenwidth()
tela_altura = root.winfo_screenheight()

# Calcula a posição para centralizar a janela
centro_x = int(tela_largura / 2 - janela_largura / 2)
centro_y = int(tela_altura / 2 - janela_altura / 2)

# Define tamanho e posição
root.geometry(
    f"{janela_largura}x{janela_altura}+{centro_x}+{centro_y}"
)


# ============================================================
# CONFIGURAÇÕES DA JANELA
# ============================================================

# Permite redimensionar a janela
root.resizable(True, True)

# Tamanho mínimo
root.minsize(300, 200)

# Tamanho máximo
root.maxsize(600, 500)

# Opacidade da janela
# 0.0 = transparente
# 1.0 = totalmente visível
root.attributes("-alpha", 0.7)


# ============================================================
# LABEL — RÓTULOS
# ============================================================

message1 = tk.Label(
    root,
    text="Hello, World!",
    bg="black",
    fg="white"
)

message2 = tk.Label(
    root,
    text="Aula dia 24/07",
    bg="black",
    fg="white"
)

# Posiciona os Labels
message1.pack(pady=5)
message2.pack(pady=5)


# ============================================================
# BUTTON — BOTÃO 1
# ============================================================

def button1_command():
    messagebox.showinfo(
        "Atenção",
        "Botão 1 foi clicado!"
    )


button1 = tk.Button(
    root,
    text="Clique aqui",
    command=button1_command
)

button1.pack(pady=6)


# ============================================================
# BUTTON — BOTÃO 2
# ============================================================

def button2_command():
    messagebox.showinfo(
        "Aviso",
        "Botão 2 foi clicado!"
    )


button2 = tk.Button(
    root,
    text="Clique aqui",
    command=button2_command
)

button2.pack(pady=5)


# ============================================================
# ENTRY — CAPTURANDO DADOS DO USUÁRIO
# ============================================================

def mostrar_nome():
    nome = entry.get()

    messagebox.showinfo(
        "Nome completo",
        nome
    )


# Label
label_nome = tk.Label(
    root,
    text="Digite seu nome completo:",
    bg="black",
    fg="white"
)

# Campo de entrada
entry = tk.Entry(root)

# Botão
button_nome = tk.Button(
    root,
    text="Mostrar",
    command=mostrar_nome
)

# Posicionando
label_nome.pack(pady=5)
entry.pack(pady=5)
button_nome.pack(pady=5)


# ============================================================
# IMAGEM — BATMAN
# ============================================================

# Carrega a imagem
Batman = tk.PhotoImage(
    file="Janela Básica/img/Batman.png"
)

# Cria um Label para exibir a imagem
imagem_batman = tk.Label(
    root,
    image=Batman,
    bg="black"
)

imagem_batman.pack(
    expand=True
)


# ============================================================
# CHECKBUTTON — CAIXA DE SELEÇÃO
# ============================================================

# Variável que armazena o estado do Checkbutton
checkbox_estado = tk.IntVar()


def mostrar_estado():
    if checkbox_estado.get():
        txt = "Checked"
    else:
        txt = "Unchecked"

    checkbox.config(
        text=f"Check me! ({txt})"
    )


# Cria o Checkbutton
checkbox = tk.Checkbutton(
    root,
    text="Check me!",
    variable=checkbox_estado,
    command=mostrar_estado,
    bg="black",
    fg="white",
    selectcolor="black"
)

# Começa marcado
checkbox.select()

# Posiciona
checkbox.pack(
    expand=True
)


# ============================================================
# LOOP PRINCIPAL
# ============================================================

root.mainloop()

