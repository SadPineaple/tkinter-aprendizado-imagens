import tkinter as tk
from PIL import ImageTk, Image

class Tela:
    def __init__(self, master):
        self.nossaTela = master

        img = Image.open("Python.png")
        self.minhaImagem = ImageTk.PhotoImage(img)
        self.lbl = tk.Label(self.nossaTela, image = self.minhaImagem)
        self.lbl.image = self.minhaImagem
        self.lbl.pack()


janelaRaiz = tk.Tk()
Tela(janelaRaiz)
janelaRaiz.mainloop()