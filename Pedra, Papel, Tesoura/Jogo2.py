from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random

# CORES DA INTERFACE

cor0 = "white"
cor1 = "black"
cor2 = "orange"
cor3 = "yellow"
cor4 = "green"
cor5 = "red"
fundo = "gray"


# CRIAÇÃO DA JANELA

janela = Tk()

janela.title("Pedra, Papel, Tesoura")

janela.geometry("260x330")

janela.configure(bg=fundo)


# ==================================================== PLACAR ====================================================

# FRAME DE CIMA

frame_cima = Frame(
    janela,
    width=260,
    height=100,
    bg=cor1,
    relief="raised"
)

frame_cima.grid(
    row=0,
    column=0,
    sticky=NW
)


# FRAME DE BAIXO

frame_baixo = Frame(
    janela,
    width=260,
    height=300,
    bg=cor0,
    relief="flat"
)

frame_baixo.grid(
    row=1,
    column=0,
    sticky=NW
)


# ==================================================== JOGADOR ====================================================

app_pessoa = Label(
    frame_cima,
    text="jogador",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 10 bold")
)

app_pessoa.place(
    x=10,
    y=70
)


# LINHA DO JOGADOR

app_pessoa_linha = Label(
    frame_cima,
    text="",
    height=10,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 10 bold")
)

app_pessoa_linha.place(
    x=0,
    y=0
)


# PONTOS DO JOGADOR

app_pessoa_pontos = Label(
    frame_cima,
    text="0",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold")
)

app_pessoa_pontos.place(
    x=50,
    y=20
)


# ==================================================== VS ====================================================

app_vs = Label(
    frame_cima,
    text=":",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold")
)

app_vs.place(
    x=125,
    y=20
)


# ==================================================== PC ====================================================

app_PC = Label(
    frame_cima,
    text="PC",
    height=9,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 10 bold")
)

app_PC.place(
    x=210,
    y=6
)


# LINHA DO PC

app_PC_linha = Label(
    frame_cima,
    text="",
    height=10,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 10 bold")
)

app_PC_linha.place(
    x=255,
    y=0
)


# PONTOS DO PC

app_PC_pontos = Label(
    frame_cima,
    text="0",
    height=1,
    anchor="center",
    bg=cor1,
    fg=cor0,
    font=("Ivy 30 bold")
)

app_PC_pontos.place(
    x=185,
    y=20
)


# ==================================================== EMPATE ====================================================

app_empate = Label(
    frame_cima,
    text="",
    height=10,
    anchor="center",
    bg=cor1,
    fg=cor3,
    font=("Ivy 10 bold")
)

app_empate.place(
    y=95,
    width=270
)

# ============================ INICIAR JOGO ======================================================================

rodadas = 5

def jogar(escolha):
    global rodadas

    print(escolha)

    opçoes = ["pedra", "papel", "tesoura"]

    if rodadas > 0:

        escolha_PC = random.choice(opçoes)
        escolha_pessoa = escolha

        print(escolha_pessoa, escolha_PC)

        rodadas -= 1

    else:
        terminar_jogo()


def terminar_jogo():
    print("Fim de jogo!")


def iniciar_jogo():

    # Faz os botões aparecerem
    btn_pedra.place(
        x=15,
        y=30
    )

    btn_papel.place(
        x=100,
        y=30
    )

    btn_tesoura.place(
        x=190,
        y=30
    )

    # Esconde o botão Jogar
    btn_iniciar.place_forget()

# ============================ IMAGENS ============================================

# PEDRA

icone_pedra = Image.open("./img/pedra.png")

icone_pedra = icone_pedra.resize(
    (50, 50),
    Image.Resampling.LANCZOS
)

icone_pedra = ImageTk.PhotoImage(icone_pedra)


btn_pedra = Button(
    frame_baixo,
    width=50,
    height=50,
    image=icone_pedra,
    bg=cor0,
    fg=cor0,
    compound="center",
    relief="flat",
    command=lambda: jogar("pedra")

)


# ================================== PAPEL =========================================

icone_papel = Image.open("./img/papel.png")

icone_papel = icone_papel.resize(
    (50, 50),
    Image.Resampling.LANCZOS
)

icone_papel = ImageTk.PhotoImage(icone_papel)


btn_papel = Button(
    frame_baixo,
    width=50,
    height=50,
    image=icone_papel,
    bg=cor0,
    fg=cor0,
    compound="center",
    relief="flat",
    command=lambda: jogar("papel")
)

# ================================== TESOURA ==============================================

icone_tesoura = Image.open("./img/tesoura.png")

icone_tesoura = icone_tesoura.resize(
    (50, 50),
    Image.Resampling.LANCZOS
)

icone_tesoura = ImageTk.PhotoImage(icone_tesoura)


btn_tesoura = Button(
    frame_baixo,
    width=50,
    height=50,
    image=icone_tesoura,
    bg=cor0,
    fg=cor0,
    compound="center",
    relief="flat",
    command=lambda: jogar("tesoura")
)


# ============================ BOTÃO JOGAR ============================

btn_iniciar = Button(
    frame_baixo,
    text="Jogar",
    bg="black",
    fg="white",
    width=30,
    height=2,
    command=iniciar_jogo
)

btn_iniciar.place(
    x=20,
    y=150
)


janela.mainloop()
