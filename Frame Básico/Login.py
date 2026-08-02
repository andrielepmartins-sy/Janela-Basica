import tkinter as tk 

from tkinter import messagebox  

root = tk.Tk()
root.title("Login")
root.geometry("300x400")
root.config(bg="white")

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

Label_usuario = tk.Label (root,
                          text="Usuário:",
                          bg="white",
                          fg="black"
)

Label_usuario.pack()

usuario = tk.Entry (root,
                  bg="white")

usuario.pack (pady=10)

#-------------------------- SENHA --------------------------------

Label_senha = tk.Label (root,
                          text="Senha:",
                          bg="white",
                          fg="black"
)

Label_senha.pack(pady=10)

senha= tk.Entry (root,
                  bg="white")

senha.pack ()

#--------------------------- BOTÃO DE "ENTRE" ---------------------

Botão_login = tk.Button (root,
                          text="Entre",
                          bg="black",
                          fg="white",
                          width=20 
)

Botão_login.pack(pady=20)

root.mainloop()