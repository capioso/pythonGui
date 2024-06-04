import tkinter as tk


class CentralPageView:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE PREVENCIÓN DE RIESGOS EN LA EMPRESA TAUNUS SRL")
        self.root.geometry("1450x600")
        self.panel = tk.Frame(self.root, bg="lightblue", height=550)
        self.panel.pack_propagate(False)
        self.panel.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def reborn(self):
        self.panel.destroy()
        self.panel = tk.Frame(self.root, bg="lightblue", height=550)
        self.panel.pack_propagate(False)
        self.panel.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def addButtons(self, button_data):
        buttonFrame = tk.Frame(self.root)
        for i, (text, command) in enumerate(button_data):
            button = tk.Button(buttonFrame, text=text, command=command, width=35,
                               font=("Calibri", 10, "bold"))
            button.grid(row=0, column=i, padx=10, pady=10)
        buttonFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def getPanel(self):
        return self.panel
