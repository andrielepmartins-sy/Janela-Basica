from tkinter import *
from PIL import Image, ImageTk
import random


# =========================================================
# CORES
# =========================================================

cor_branco = "white"
cor_preto = "black"
cor_amarelo = "yellow"
cor_verde = "green"
cor_vermelho = "red"
cor_fundo = "gray"


# =========================================================
# JANELA
# =========================================================

janela = Tk()

janela.title("Pedra, Papel, Tesoura")

janela.geometry("260x330")

janela.configure(bg=cor_fundo)

janela.resizable(False, False)


# =========================================================
# FRAME SUPERIOR - PLACAR
# =========================================================

frame_cima = Frame(
    janela,
    width=260,
    height=130,
    bg=cor_preto
)

frame_cima.place(
    x=0,
    y=0
)


# =========================================================
# FRAME INFERIOR - JOGO
# =========================================================

frame_baixo = Frame(
    janela,
    width=260,
    height=200,
    bg=cor_branco
)

frame_baixo.place(
    x=0,
    y=130
)


# =========================================================
# JOGADOR
# =========================================================

app_pessoa_pontos = Label(
    frame_cima,
    text="0",
    bg=cor_preto,
    fg=cor_branco,
    font=("Ivy", 30, "bold")
)

app_pessoa_pontos.place(
    x=52,
    y=15
)


app_pessoa = Label(
    frame_cima,
    text="jogador",
    bg=cor_preto,
    fg=cor_branco,
    font=("Ivy", 10, "bold")
)

app_pessoa.place(
    x=10,
    y=90
)


# =========================================================
# DOIS PONTOS NO CENTRO
# =========================================================

app_vs = Label(
    frame_cima,
    text=":",
    bg=cor_preto,
    fg=cor_branco,
    font=("Ivy", 30, "bold")
)

app_vs.place(
    x=125,
    y=15
)


# =========================================================
# PC
# =========================================================

app_PC_pontos = Label(
    frame_cima,
    text="0",
    bg=cor_preto,
    fg=cor_branco,
    font=("Ivy", 30, "bold")
)

app_PC_pontos.place(
    x=187,
    y=15
)


app_PC = Label(
    frame_cima,
    text="PC",
    bg=cor_preto,
    fg=cor_branco,
    font=("Ivy", 10, "bold")
)

app_PC.place(
    x=210,
    y=90
)


# =========================================================
# LINHA VERDE DO JOGADOR
# =========================================================

linha_jogador = Frame(
    frame_cima,
    width=130,
    height=3,
    bg=cor_verde
)

linha_jogador.place(
    x=0,
    y=126
)

# Começa escondida
linha_jogador.place_forget()


# =========================================================
# LINHA VERDE DO PC
# =========================================================

linha_pc = Frame(
    frame_cima,
    width=130,
    height=3,
    bg=cor_verde
)

linha_pc.place(
    x=130,
    y=126
)

# Começa escondida
linha_pc.place_forget()


# =========================================================
# LINHA AMARELA - EMPATE
# =========================================================

linha_empate = Frame(
    frame_cima,
    width=260,
    height=3,
    bg=cor_amarelo
)

linha_empate.place(
    x=0,
    y=126
)


# =========================================================
# VARIÁVEIS DO JOGO
# =========================================================

rodadas = 5

pontos_pessoa = 0

pontos_pc = 0

empates = 0


# =========================================================
# FUNÇÃO PARA JOGAR
# =========================================================

def jogar(escolha):

    global rodadas
    global pontos_pessoa
    global pontos_pc
    global empates

    if rodadas <= 0:
        return


    # =====================================================
    # ESCOLHAS
    # =====================================================

    opcoes = [
        "pedra",
        "papel",
        "tesoura"
    ]

    escolha_pc = random.choice(opcoes)


    print("-----------------------------")
    print("Jogador:", escolha)
    print("PC:", escolha_pc)


    # =====================================================
    # EMPATE
    # =====================================================

    if escolha == escolha_pc:

        empates += 1

        print("EMPATE!")


        # Esconde as linhas verdes
        linha_jogador.place_forget()
        linha_pc.place_forget()


        # Mostra linha amarela inteira
        linha_empate.place(
            x=0,
            y=126
        )


    # =====================================================
    # JOGADOR GANHOU
    # =====================================================

    elif (
        escolha == "pedra"
        and escolha_pc == "tesoura"

        or

        escolha == "papel"
        and escolha_pc == "pedra"

        or

        escolha == "tesoura"
        and escolha_pc == "papel"
    ):

        pontos_pessoa += 1

        print("JOGADOR GANHOU!")


        # Esconde linha amarela
        linha_empate.place_forget()

        # Esconde linha do PC
        linha_pc.place_forget()


        # Mostra linha verde do jogador
        linha_jogador.place(
            x=0,
            y=126
        )


        # Atualiza placar
        app_pessoa_pontos.config(
            text=str(pontos_pessoa)
        )


    # =====================================================
    # PC GANHOU
    # =====================================================

    else:

        pontos_pc += 1

        print("PC GANHOU!")


        # Esconde linha amarela
        linha_empate.place_forget()

        # Esconde linha do jogador
        linha_jogador.place_forget()


        # Mostra linha verde do PC
        linha_pc.place(
            x=130,
            y=126
        )


        # Atualiza placar
        app_PC_pontos.config(
            text=str(pontos_pc)
        )


    # =====================================================
    # DIMINUI UMA RODADA
    # =====================================================

    rodadas -= 1

    print("Rodadas restantes:", rodadas)


    # =====================================================
    # FIM DO JOGO
    # =====================================================

    if rodadas == 0:
        terminar_jogo()


# =========================================================
# TERMINAR JOGO
# =========================================================

def terminar_jogo():

    print("-----------------------------")
    print("FIM DE JOGO!")


    # Esconder os botões
    btn_pedra.place_forget()
    btn_papel.place_forget()
    btn_tesoura.place_forget()


    # =====================================================
    # JOGADOR VENCEU
    # =====================================================

    if pontos_pessoa > pontos_pc:

        print("VOCÊ VENCEU!")


        linha_pc.place_forget()
        linha_empate.place_forget()


        linha_jogador.place(
            x=0,
            y=126
        )


    # =====================================================
    # PC VENCEU
    # =====================================================

    elif pontos_pc > pontos_pessoa:

        print("PC VENCEU!")


        linha_jogador.place_forget()
        linha_empate.place_forget()


        linha_pc.place(
            x=130,
            y=126
        )


    # =====================================================
    # EMPATE FINAL
    # =====================================================

    else:

        print("EMPATE!")


        linha_jogador.place_forget()
        linha_pc.place_forget()


        linha_empate.place(
            x=0,
            y=126
        )


    # =====================================================
    # BOTÃO REINICIAR
    # =====================================================

    btn_iniciar.config(
        text="Reiniciar"
    )

    btn_iniciar.place(
        x=20,
        y=145
    )


# =========================================================
# REINICIAR JOGO
# =========================================================

def iniciar_jogo():

    global rodadas
    global pontos_pessoa
    global pontos_pc
    global empates


    # =====================================================
    # RESETAR VALORES
    # =====================================================

    rodadas = 5

    pontos_pessoa = 0

    pontos_pc = 0

    empates = 0


    # =====================================================
    # RESETAR PLACAR
    # =====================================================

    app_pessoa_pontos.config(
        text="0"
    )

    app_PC_pontos.config(
        text="0"
    )


    # =====================================================
    # RESETAR LINHAS
    # =====================================================

    linha_jogador.place_forget()

    linha_pc.place_forget()


    # Amarela inteira novamente
    linha_empate.place(
        x=0,
        y=126
    )


    # =====================================================
    # MOSTRAR BOTÕES
    # =====================================================

    btn_pedra.place(
        x=15,
        y=20
    )

    btn_papel.place(
        x=100,
        y=20
    )

    btn_tesoura.place(
        x=185,
        y=20
    )


    # =====================================================
    # ESCONDER BOTÃO JOGAR
    # =====================================================

    btn_iniciar.place_forget()


# =========================================================
# IMAGEM - PEDRA
# =========================================================

icone_pedra = Image.open(
    "./img/pedra.png"
)

icone_pedra = icone_pedra.resize(
    (50, 50),
    Image.Resampling.LANCZOS
)

icone_pedra = ImageTk.PhotoImage(
    icone_pedra
)


btn_pedra = Button(
    frame_baixo,
    width=50,
    height=50,
    image=icone_pedra,
    bg=cor_branco,
    activebackground=cor_branco,
    relief="flat",
    borderwidth=0,
    command=lambda: jogar("pedra")
)


# =========================================================
# IMAGEM - PAPEL
# =========================================================

icone_papel = Image.open(
    "./img/papel.png"
)

icone_papel = icone_papel.resize(
    (50, 50),
    Image.Resampling.LANCZOS
)

icone_papel = ImageTk.PhotoImage(
    icone_papel
)


btn_papel = Button(
    frame_baixo,
    width=50,
    height=50,
    image=icone_papel,
    bg=cor_branco,
    activebackground=cor_branco,
    relief="flat",
    borderwidth=0,
    command=lambda: jogar("papel")
)


# =========================================================
# IMAGEM - TESOURA
# =========================================================

icone_tesoura = Image.open(
    "./img/tesoura.png"
)

icone_tesoura = icone_tesoura.resize(
    (50, 50),
    Image.Resampling.LANCZOS
)

icone_tesoura = ImageTk.PhotoImage(
    icone_tesoura
)


btn_tesoura = Button(
    frame_baixo,
    width=50,
    height=50,
    image=icone_tesoura,
    bg=cor_branco,
    activebackground=cor_branco,
    relief="flat",
    borderwidth=0,
    command=lambda: jogar("tesoura")
)


# =========================================================
# BOTÃO JOGAR
# =========================================================

btn_iniciar = Button(
    frame_baixo,
    text="Jogar",
    bg=cor_preto,
    fg=cor_branco,
    activebackground=cor_preto,
    activeforeground=cor_branco,
    width=30,
    height=2,
    relief="flat",
    command=iniciar_jogo
)

btn_iniciar.place(
    x=20,
    y=145
)


# =========================================================
# INICIAR
# =========================================================

janela.mainloop()