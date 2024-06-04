import tkinter as tk


class GraphsPageView:
    def __init__(self, root):
        self.root = root
        self.panel = tk.Frame(self.root, bg="yellow", height=550)
        self.panel.pack(side=tk.BOTTOM, fill=tk.BOTH)
        label = tk.Label(self.panel, text="Pagina 3", bg="red", fg="white", font=("Calibri", 14, "bold"))
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)