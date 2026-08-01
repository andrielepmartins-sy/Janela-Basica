import tkinter as tk

root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("400x350")
root.configure(bg="black")

# CALCULO =======================================================================

def calcular_imc():
    try:
        peso = float(Peso.get().replace(",","."))
        altura = float(Altura.get().replace(",","."))

        imc = peso / (altura ** 2)

        if imc < 18.5:
            classificacao = "Magreza"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        elif imc < 35:
            classificacao = "Obesidade grau I"
        elif imc < 40:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III"

        label_resultado.config(
            text=f"Seu IMC é: {imc:.2f}\nClassificação: {classificacao}"
        )

    except ValueError:
        label_resultado.config(
            text="Digite um peso e uma altura válidos!"
        )

# PESO ===========================================================================

label_peso = tk.Label( root, 
                      text="Peso (kg)", 
                      fg="white", 
                      bg="black",
                      width=15
                      )
label_peso.pack(pady=(68, 5))

Peso = tk.Entry(root, justify="center")
Peso.pack(pady=5)

# ALTURA ==========================================================================

label_altura = tk.Label( root, 
                        text="Altura (m)", 
                        fg="white",
                        bg="black",
                        width=15)
label_altura.pack()

Altura = tk.Entry(root, justify="center")
Altura.pack(pady=5)

# BOTÃO ============================================================================

botao = tk.Button(root, 
                  text="Calcular", 
                  command=calcular_imc,
                  bg="green", 
                  fg="white",
                  width=10)
botao.pack(pady=15)

# RESULTADO =========================================================================

label_resultado = tk.Label( root, 
                           text="Preencha os campos e clique em calcular.", 
                           fg="white", 
                           bg="black")
label_resultado.pack(pady=(10, 8))

# POSIÇÃO ===========================================================================

janela_largura = 400
janela_altura = 300

tela_largura = root.winfo_screenwidth()
tela_altura = root.winfo_screenheight()

centro_x = int(tela_largura / 2 - janela_largura / 2)
centro_y = int(tela_altura / 2 - janela_altura / 2)

root.geometry(
    f"{janela_largura}x{janela_altura}+{centro_x}+{centro_y}"
)


root.mainloop()