import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

# ---------------- JANELA ----------------

root = tk.Tk()
root.title("Login")
root.geometry("350x450")
root.configure(bg="white")
root.resizable(False, False)

# ---------------- TÍTULO ----------------

titulo = tk.Label(
    root,
    text="Faça seu login",
    font=("Arial", 22, "bold"),
    bg="white"
)
titulo.pack(pady=15)

# ---------------- IMAGEM ----------------

caminho_imagem = os.path.join(
    os.path.dirname(__file__),
    "img",
    "profile.png"
)

try:
    imagem_pil = Image.open(caminho_imagem)
    imagem_pil = imagem_pil.resize((120, 120))

    foto = ImageTk.PhotoImage(imagem_pil)

    imagem = tk.Label(root, image=foto, bg="white")
    imagem.image = foto
    imagem.pack(pady=10)

except Exception as erro:
    print(erro)

    imagem = tk.Label(
        root,
        text="👤",
        font=("Arial", 70),
        bg="white"
    )
    imagem.pack(pady=10)

# ---------------- USUÁRIO ----------------

tk.Label(root, text="Usuário", bg="white", anchor="w").pack(fill="x", padx=40)

entry_usuario = tk.Entry(root)
entry_usuario.pack(fill="x", padx=40, pady=5)

# ---------------- SENHA ----------------

tk.Label(root, text="Senha", bg="white", anchor="w").pack(fill="x", padx=40)

entry_senha = tk.Entry(root, show="*")
entry_senha.pack(fill="x", padx=40, pady=5)

# ---------------- FUNÇÃO ----------------

def entrar():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "1234":
        messagebox.showinfo("Login", "Login realizado com sucesso!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

# ---------------- BOTÃO ----------------

tk.Button(
    root,
    text="Entrar",
    command=entrar
).pack(fill="x", padx=40, pady=15)

# ---------------- PARTE INFERIOR ----------------

frame = tk.Frame(root, bg="white")
frame.pack(fill="x", padx=35)

lembrar = tk.BooleanVar()

tk.Checkbutton(
    frame,
    text="Lembrar-me",
    variable=lembrar,
    bg="white"
).pack(side="left")

tk.Label(
    frame,
    text="Esqueceu sua senha?",
    fg="blue",
    bg="white",
    cursor="hand2"
).pack(side="right")

root.mainloop()