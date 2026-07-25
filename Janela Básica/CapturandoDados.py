import tkinter as tk 
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")

#capturando dados do usuário
def button_command():
    nome = entry.get()
    messagebox.showinfo("Nome completo", nome)

#campo de entrada e botão
label = tk.Label(root, text="Digite seu nome completo:")
entry = tk.Entry(root)
button = tk.Button(root, text="Mostrar", command=button_command)

#organizando os elementos na janela
label.pack(pady=5)
entry.pack(pady=5)  
button.pack(pady=5)

root.mainloop()
