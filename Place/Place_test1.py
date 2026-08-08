import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.geometry("300x300+50+50")

def mostrar_selecao(event):
    selecao = cidades.curselection()
    messagebox.showinfo("Seleção", cidades.get(selecao))   

tk.Label(root, text="Qual cidade você gostaria de visitar?").place(x=50, y=20)

cidades = tk.Listbox(root, selectmode=tk.SINGLE, width=24)
cidades.place(x=40, y=65)

for cidade in ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"]:
    cidades.insert(tk.END, cidade)

cidades.bind("<<ListboxSelect>>", mostrar_selecao)

botao = tk.Button(root, text="Sair", command=quit)
botao.place(x=125, y=250)

root.mainloop()