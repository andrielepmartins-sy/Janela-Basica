from tkinter import Tk, Canvas


# =========================
# CONFIGURAÇÃO DA JANELA
# =========================
CANVAS_W =  400
CANVAS_H = 800
janela = Tk()
janela.geometry(f"{CANVAS_H}x{CANVAS_W}")

janela.title("Desenho da Casa")


# =========================
# CONFIGURAÇÃO DO CANVAS
# =========================

canvas = Canvas(
    janela,
    width=900,
    height=900,
    bg="blue"
)


# =========================
# GRAMA
# =========================

canvas.create_line(
    900, 380,
    0, 380,
    fill="green",
    width=90
)


# =========================
# CASA
# =========================

canvas.create_rectangle(
    390, 380,
    110, 180,
    fill="pink"
)


# =========================
# TELHADO
# =========================

canvas.create_polygon(
    253, 100,
    80, 190,
    420, 190,
    fill="black"
)


# =========================
# PORTA
# =========================

canvas.create_rectangle(
    280, 380,
    210, 260,
    fill="white"
)

# Maçaneta da porta
canvas.create_oval(
    270, 320,
    260, 330,
    fill="white",
    width=1
)


# =========================
# JANELA ESQUERDA
# =========================

canvas.create_rectangle(
    190, 300,
    130, 240,
    fill="white"
)

# Divisão horizontal
canvas.create_line(
    190, 270,
    130, 270,
    fill="black",
    width=2
)

# Divisão vertical
canvas.create_line(
    160, 300,
    160, 240,
    fill="black",
    width=2
)


# =========================
# JANELA DIREITA
# =========================

canvas.create_rectangle(
    300, 300,
    370, 240,
    fill="white"
)

# Divisão vertical
canvas.create_line(
    335, 300,
    335, 240,
    fill="black",
    width=2
)

# Divisão horizontal
canvas.create_line(
    300, 270,
    370, 270,
    fill="black",
    width=2
)


# =========================
# SOL
# =========================

canvas.create_oval(
    50, 50,
    120, 120,
    fill="yellow"
)

# =========================
# CARRO
# =========================

canvas.create_rectangle(
    460, 250, 
    600, 330,
    fill='purple',
)

# =========================
# EXECUÇÃO
# =========================

canvas.pack()
janela.mainloop()