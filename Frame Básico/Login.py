import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("300x220")
root.config(bg="black")


def entrar():
    nome = usuario.get()
    senha_digitada = senha.get()

    if nome == "admin" and senha_digitada == "1234":
        resultado.config(text="Login realizado com sucesso!", fg="green")
    else:
        resultado.config(text="Usuário ou senha incorretos!", fg="red")


tk.Label(root,
         text="Faça seu login",
         bg="black",
         fg="white",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root,
         text="Usuário:",
         fg="white",
         bg="black").pack()

usuario = tk.Entry(root, justify="center")
usuario.pack(pady=5)

tk.Label(root,
         text="Senha:",
         fg="white",
         bg="black").pack()

senha = tk.Entry(root, justify="center", show="*")
senha.pack(pady=5)

botao = tk.Button(root,
                  text="Entrar",
                  command=entrar,
                  bg="blue",
                  fg="white",
                  width=20)
botao.pack(pady=15)

resultado = tk.Label(root, text="", bg="black", fg="white")
resultado.pack()

root.mainloop()