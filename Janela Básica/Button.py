import tkinter as tk

#Função para exibir uma mensagem quando o botão for clicado
from tkinter import messagebox

#cria a janela principal
root = tk.Tk()  
root.geometry("400x300")

#informa que o botão foi clicado
def button_command():
    messagebox.showinfo("Atenção", "Botão1 clicado!")

#cria um botão e associa a função button_command ao evento de clique
button = tk.Button(root, text="Clique aqui", command=button_command)

button.pack()

def button_command():
    messagebox.showinfo("Aviso", "Botão2 foi clicado!")

button = tk.Button(root, text="Clique aqui", command=button_command)

button.pack()

root.mainloop()