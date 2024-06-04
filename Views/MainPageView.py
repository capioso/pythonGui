import tkinter as tk

from PIL import ImageTk, Image


class MainPageView:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE PREVENCION DE RIESGOS EN LA EMPRESA TAUNUS SRL")
        self.root.geometry("900x600")

        self.label = tk.Label(root, text="SISTEMA DE PREVENCION DE RIESGOS EN LA EMPRESA TAUNUS SRL",
                              font=("Calibri", 13, "bold"), pady=20)
        self.label.pack()

        img = ImageTk.PhotoImage(Image.open("Images/logo.png"))
        self.panel = tk.Label(root, image=img)
        self.panel.image = img
        self.panel.pack(fill="both", pady=40)

    def addButton(self, text, command):
        button_width = 40
        fontConfig = ("Calibri", 12, "bold")
        button = tk.Button(self.root, text=text, command=command, width=button_width, anchor='w', font=fontConfig,
                           pady=20)
        button.pack()

    def getRoot(self):
        return self.root