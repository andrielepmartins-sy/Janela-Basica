from tkinter import Tk, Canvas

janela = Tk()
janela.geometry("500x400")
canvas= Canvas(janela, width=400, height=300, bg="yellow") 


canvas.create_text(200, 150, text='Helow', font=('Arial',20, "bold"), anchor='e', fill='red')
canvas.create_text(200, 150, text='Word', font=('Arial',20, "bold"), anchor='w', fill='blue')

canvas.pack()
janela.mainloop()
