import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.geometry("400x300")
root.configure(bg="black" )

def enter_pressionado(event):
    label.config(text=event.widget.get())
def Tab_pressionado(event):
    label.config(text=event.widget.get())

entry = tk.Entry(root)
entry.insert(0, "Digite seu texto")

entry.bind("<Return>", enter_pressionado)
entry.bind("<Tab>", Tab_pressionado)

entry.pack(pady=5)  

label = tk.Label(root, text="Demostração!")
label.pack()

root.mainloop()