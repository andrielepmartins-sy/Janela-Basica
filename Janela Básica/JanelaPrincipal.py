import tkinter as tk

#cria janela principal
root = tk.Tk()

# ===================================================================================

#cria um rótulo com a mensagem "Hello, World!"
message1 = tk.Label(root, text="Hello, World!")
message2 = tk.Label(root, text="Aula dia 24/07 ")

#posiciona o rótulo na janela
message1.pack(pady=5)
message2.pack(pady=5)

#define o tamanho da janela e a posição inicial
root.geometry("400x200+50+50")

#rotulo da janela
root.title("Desenvolvimento de Sistemas - Janela Básica")

#cor de fundo da minha janela
root.configure(bg="black")

# ===================================================================================

#define a largura e a altura
janela_largura = 300
janela_altura = 200

#ajusta a posição da janela no centro da tela
tela_largura = root.winfo_screenwidth()
tela_altura = root.winfo_screenheight()

#define a posição da janela no centro da tela
centro_x = int(tela_largura  / 2- janela_largura /2 )
centro_y = int(tela_altura  / 2 - janela_altura /2 )  

#define o tamanho da janela e a posição inicial
root.geometry(f"{janela_largura}x{janela_altura}+{centro_x}+{centro_y}")

# ===================================================================================

#impede que a janela seja redimensionada
root.resizable(True, True) 

#define o tamanho mínimo da janela
root.minsize(300, 200)

#define o tamanho máximo da janela
root.maxsize(600, 500)

#define a opacidade da janela (0.0 a 1.0)
root.attributes("-alpha", 0.7)

# ===================================================================================

from tkinter import messagebox

#informa que o botão foi clicado
def button_command():
    messagebox.showinfo("Atenção", "Botão1 foi clicado!")

#cria um botão e associa a função button_command ao evento de clique
button = tk.Button(root, text="Clique aqui", command=button_command)

#posiciona o botão na janela
button.pack(pady=6)

# ↳ repetição do botão com a mesma função
def button_command():
    messagebox.showinfo("Aviso", "Botão2 foi clicado!")

button = tk.Button(root, text="Clique aqui", command=button_command)

button.pack(pady=5)

# ===================================================================================

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

# ===================================================================================


#inicia o loop principal da janela
root.mainloop()