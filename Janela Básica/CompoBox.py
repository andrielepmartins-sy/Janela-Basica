import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("400x300")

def seleção_mudou(evento):
    label.config(text=f"{evento.widget.get()} selecionado!")

combobox = ttk.Combobox(root, values=["Primeiro", "Segundo", "Terceiro"])

combobox.set("Primeiro")

combobox.bind("<<ComboboxSelected>>", seleção_mudou)

combobox.pack()

label = tk.Label(root, text="Primeiro selecionado!")

label.pack()

root.mainloop()