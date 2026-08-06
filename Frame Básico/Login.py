import tkinter as tk 

from tkinter import messagebox  

root = tk.Tk()
root.title("Login")
root.geometry("300x500")
root.config(bg="white")

tk.Label(root, text="Faça seu login", font=("Arial", 16), bg="white").pack(pady=20)

# ------------------------ IMAGEM --------------------------------

Profile = tk.PhotoImage(
    file="Frame Básico/img/Profile.png"
)
Profile = Profile.subsample(4, 4)

imagem_Profile = tk.Label(
                          root,
                          image=Profile,
                          bg="white"
)

imagem_Profile.pack(pady=20)

#-------------------------- USUARIO ------------------------------

tk.Label(root, text="Usuário:", bg="white", anchor="w").pack(fill="x", padx=40)

usuario = tk.Entry (root,
                  bg="white")

usuario.pack (pady=10)


#-------------------------- SENHA --------------------------------

tk.Label(root, text="Senha:", bg="white", anchor="w").pack(fill="x", padx=40)

entry_senha = tk.Entry(root, show="*")
entry_senha.pack(pady=10)

#------------------------- FUNÇÃO DE LOGIN E SENHA ----------------

def login():
    usuario_digitado = usuario.get()
    senha_digitada = entry_senha.get()

    if usuario_digitado == "admin" and senha_digitada == "1234":
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Login", "Usuário ou senha incorretos.")

#--------------------------- BOTÃO DE "ENTRE" ---------------------

tk.Button(
    root,
    text="Entrar",
    command=login, 
    bg="black", 
    fg="white"
).pack(fill="x", padx=60, pady=20)


# ----------------- PARTE INFERIOR ----------------

frame = tk.Frame(root, bg="white")
frame.pack(fill="x", padx=30, pady=25)

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

#------------------- FINAL -----------------------------------------    
root.mainloop()