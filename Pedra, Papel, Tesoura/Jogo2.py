from tkinter import *
from tkinter import ttk
from PIL import Imagem, ImageTK
# CORES DA INTERFACE

cor0 = "white"    # Cor branca
cor1 = "black"    # Cor preta
cor2 = "orange"   # Cor laranja
cor3 = "yellow"   # Cor amarela
cor4 = "green"    # Cor verde
cor5 = "red"      # Cor vermelha
fundo = "gray"    # Cor do fundo da janela


# CRIAÇÃO DA JANELA

janela = Tk()  

janela.title("Pedra, Papel, Tesoura") 

janela.geometry("260x250")

janela.configure(bg=fundo)

#==================================================== PLACAR ========================================================================   
# FRAME DE CIMA

# Cria um Frame (área) na parte superior da janela
frame_cima = Frame(
    janela,
    width=260,       # Largura do Frame
    height=100,      # Altura do Frame
    bg=cor1,         # Fundo preto
    relief="raised"  # Efeito de relevo
)

# Posiciona o Frame na linha 0 e coluna 0
frame_cima.grid(
    row=0,
    column=0,
    sticky=NW
)

# FRAME DE BAIXO

# Cria o Frame que ficará na parte inferior
frame_baixo = Frame(
    janela,
    width=260,
    height=300,
    bg=cor0,          # Fundo branco
    relief="flat"     # Sem relevo
)

# Posiciona o Frame abaixo do frame_cima
frame_baixo.grid(
    row=1,
    column=0,
    sticky=NW
)

# NOME DO JOGADOR

# Cria um texto para identificar o jogador
app_pessoa = Label(
    frame_cima,
    text="jogador",          # Texto mostrado
    height=1,
    anchor="center",         # Centraliza o texto
    bg=cor1,                 # Fundo preto
    fg=cor0,                 # Texto branco
    font=("Ivy 10 bold")     # Fonte e tamanho
)

# Posiciona o nome do jogador
app_pessoa.place(
    x=10,
    y=70
)


# LINHA DO JOGADOR

# Cria uma área verde que poderá ser usada
# como parte da interface do jogador
app_pessoa_linha = Label(
    frame_cima,
    text="",
    height=10,
    anchor="center",
    bg=cor4,                 # Fundo verde
    fg=cor0,
    font=("Ivy 10 bold")
)

# Posiciona a linha/área verde
app_pessoa_linha.place(
    x=0,
    y=0
)


# PONTOS DO JOGADOR

# Mostra a pontuação atual do jogador
app_pessoa_pontos = Label(
    frame_cima,
    text="0",                # Pontuação inicial
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold")     # Fonte grande
)

# Posiciona a pontuação
app_pessoa_pontos.place(
    x=50,
    y=20
)

# SEPARADOR DA PONTUAÇÃO

# Cria o ":" que ficará entre os pontos
# Exemplo: 0 : 0
app_vs = Label(
    frame_cima,
    text=":",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold")
)

# Posiciona o separador
app_vs.place(
    x=125,
    y=20
)


app_PC = Label(
    frame_cima,
    text="PC",          # Texto mostrado
    height=9,
    anchor="center",         # Centraliza o texto
    bg=cor1,                 # Fundo preto
    fg=cor0,                 # Texto branco
    font=("Ivy 10 bold")     # Fonte e tamanho
)
app_PC.place(
    x=210,
    y=6
)

app_PC_linha = Label(
    frame_cima,
    text="",
    height=10,
    anchor="center",
    bg=cor4,                 # Fundo verde
    fg=cor0,
    font=("Ivy 10 bold")
)

# Posiciona a linha/área verde
app_PC_linha.place(
    x=255,
    y=0
)

app_PC_pontos = Label(
    frame_cima,
    text="0",                # Pontuação inicial
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold")     # Fonte grande
)

# Posiciona a pontuação
app_PC_pontos.place(
    x=185,
    y=20
)

app_empate = Label(
    frame_cima,
    text="",
    height=10,
    anchor="center",
    bg=cor3,                
    fg=cor3,
    font=("Ivy 10 bold")
)

# Posiciona a linha/área Amarela
app_empate.place(
    y=95,
    width=270
)

#================================================ IMAGENS ==================================================

icone_pedra = Image.open("./img/pedra.png")
icone_pedra = icone_pedra.resize((50, 50), Image.Resampling.LANCZOS)
icone_pedra = ImageTK.PhotoImage(icone_pedra)

btn_pedra = Button (frame_baixo,
                    width=50,
                    height=50,
                    image=icone_pedra,
                    bg=cor0, fg=cor0,
                    compound="center",
                    relief="flat")
btn_pedra.place(
    x=15,
    y=60
)




janela.mainloop()