import tkinter as tk

from PIL import ImageTk, Image


class MainPageView:
    tittle = "SISTEMA DE PREVENCION DE RIESGOS EN LA EMPRESA TAUNUS SRL"

    def __init__(self, root):
        self.root = root
        self.root.title(MainPageView.tittle)
        self.root.geometry("900x600")
        self.root.configure(bg='white')

        self.label = tk.Label(root,
                              text=MainPageView.tittle,
                              font=("Calibri", 13, "bold"),
                              pady=30,
                              bg='white')
        self.label.pack()

        img = ImageTk.PhotoImage(Image.open("Images/logo.png"))
        self.panel = tk.Label(root, image=img, bg='white')
        self.panel.image = img
        self.panel.pack(fill="both", pady=40)

    def addButton(self, text, command):
        button_width = 40
        fontConfig = ("Calibri", 12, "bold")
        button = tk.Button(self.root,
                           text=text,
                           command=command,
                           width=button_width,
                           anchor='w',
                           font=fontConfig,
                           background='gray',
                           foreground='white',
                           highlightbackground='black',
                           pady=15)
        button.pack(pady=(15, 0))

    def getRoot(self):
        return self.root
