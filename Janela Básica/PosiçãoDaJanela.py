import tkinter as tk    

#define a largura e a altura da janela
janela_largura = 300
janela_altura = 200

root = tk.Tk()

#define o tamanho da janela e a posição inicial
tela_largura = root.winfo_screenwidth()
tela_altura = root.winfo_screenheight()

#define a posição da janela no centro da tela
centro_x = int(tela_largura  / 2- janela_largura /2 )
centro_y = int(tela_altura  / 2 - janela_altura /2 )  

#define o tamanho da janela e a posição inicial
root.geometry(f"{janela_largura}x{janela_altura}+{centro_x}+{centro_y}")

root.mainloop()