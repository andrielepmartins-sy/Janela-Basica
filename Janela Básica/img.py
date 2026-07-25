import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

#puxando a imagem do Batman
Batman = tk.PhotoImage(file="Janela Básica/img/Batman.png")

#em seguida, criando um label para exibir a imagem
label = tk.Label(root, image=Batman)
label.pack(expand=True)


root.mainloop()
