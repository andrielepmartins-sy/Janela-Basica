import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.configure(bg="white")

janela_largura = 400
janela_altura = 200

tela_largura = root.winfo_screenwidth()
tela_altura = root.winfo_screenheight()

centro_x = int(tela_largura / 2 - janela_largura / 2)
centro_y = int(tela_altura / 2 - janela_altura / 2)

root.geometry(
    f"{janela_largura}x{janela_altura}+{centro_x}+{centro_y}"
)

# ---------------- IMAGEM ----------------

perfil = tk.PhotoImage(file="Grid/img/Perfil.png")
perfil = perfil.subsample(4, 4)

imagem = tk.Label(root, image=perfil, bg="white")
imagem.grid(row=1, column=0, rowspan=6, padx=10, pady=10)


# ---------------- NOME ----------------

tk.Label(root, text="Nome", bg="white").grid(row=1, column=1, padx=5, pady=5, sticky="w")

entry_nome = tk.Entry(root, width=25)
entry_nome.grid(row=1, column=2, padx=5, pady=5)

# ---------------- GÊNERO ----------------

tk.Label(root, text="Gênero", bg="white").grid(row=2, column=1, padx=5, pady=5, sticky="w")
genero = ttk.Combobox(
    root,
    values=["Masculino", "Feminino", "Transgênero" "Outro"],
    state="readonly",
    width=22,
    cursor="hand2"
)
genero.grid(row=2, column=2, padx=5, pady=5)

# ---------------- COR DOS OLHOS ----------------

tk.Label(root, text="Cor dos olhos", bg="white").grid(row=3, column=1, padx=5, pady=5, sticky="w")

olhos = ttk.Combobox(
    root,
    values=["Castanho", "Azul", "Verde", "Preto", "Mel"],
    state="readonly",
    width=22,
    cursor="hand2"
)
olhos.grid(row=3, column=2, padx=5, pady=5)

# ---------------- ALTURA ----------------

tk.Label(root, text="Altura (cm)", bg="white").grid(row=4, column=1, padx=5, pady=5, sticky="w")

entry_altura = tk.Entry(root, width=25)
entry_altura.grid(row=4, column=2, padx=5, pady=5)

# ---------------- PESO ----------------

tk.Label(root, text="Peso (kg)", bg="white").grid(row=5, column=1, padx=5, pady=5, sticky="w")

entry_peso = tk.Entry(root, width=25)
entry_peso.grid(row=5, column=2, padx=5, pady=5)

# ---------------- BOTÃO ----------------

def enviar():
    messagebox.showinfo("Dados", f"\n Nome: {entry_nome.get()}\n Cor dos Olhos: {olhos.get()}\n Altura: {entry_altura.get()}\n Peso: {entry_peso.get()}")


btn = tk.Button(root, text="Enviar", command=enviar, cursor="hand2")
btn.grid(row=6, column=2, padx=5, pady=5, sticky="e")

root.mainloop()