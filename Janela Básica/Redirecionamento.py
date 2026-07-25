import tkinter as tk

root = tk.Tk()

#define o tamanho da janela e a posição inicial
root.geometry("400x300")

#impede que a janela seja redimensionada
root.resizable(True, True) 

#define o tamanho mínimo da janela
root.minsize(300, 200)

#define o tamanho máximo da janela
root.maxsize(800, 600)

root.mainloop()