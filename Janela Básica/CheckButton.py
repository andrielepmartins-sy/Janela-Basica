import tkinter as tk

root = tk.Tk()

root.geometry("400x300")

checkbox_estado = tk.IntVar()  # Variável para armazenar o estado do checkbox

def mostrar_estado():
    if checkbox_estado.get():
        txt = "Checked"
    else:
        txt = "Unchecked"
    checkbox.config(
        text=f"Check me! ({txt})")

checkbox = tk.Checkbutton(root, text="Check me! (Checked)", variable=checkbox_estado, command=mostrar_estado)

checkbox.select()

checkbox.pack(expand=True)

root.mainloop()

    