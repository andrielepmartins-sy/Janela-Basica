import tkinter as tk

root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("400x350")
root.configure(bg="black")


def calcular_imc():
    try:
        peso = float(Peso.get())
        altura = float(Altura.get())

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

titulo = tk.Label(root, text="Calculadora de IMC", fg="white", bg="black")
titulo.pack(pady=10)

label_peso = tk.Label( root, text="Peso (kg)", fg="white", bg="black")
label_peso.pack()

Peso = tk.Entry(root, justify="center")
Peso.pack(pady=5)

label_altura = tk.Label( root, text="Altura (m)", fg="white",bg="black")
label_altura.pack()

Altura = tk.Entry(root, justify="center")
Altura.pack(pady=5)

botao = tk.Button(root, text="Calcular IMC", command=calcular_imc, width=20)
botao.pack(pady=15)

label_resultado = tk.Label( root, text="Informe seu peso e sua altura.", fg="white", bg="black")
label_resultado.pack(pady=10)

root.mainloop()