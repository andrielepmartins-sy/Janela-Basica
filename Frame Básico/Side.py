import tkinter as tk 

root = tk.Tk()
root.title("SENAI - Desenvolvimento de Sistemas")
root.config(bg="black")

frame = tk.Frame(root, width=200, height=200)
frame.pack(padx=10, pady=10)

a_frame = tk.Frame(frame, width=190, height=190, bg="red")
a_frame.pack(side="left", padx=10, pady=10)

b_frame = tk.Frame(frame, width=190, height=190, bg="red")
b_frame.pack(side="right", padx=10, pady=10)

root.mainloop()

#top
#bottom