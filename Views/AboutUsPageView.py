import tkinter as tk


class AboutUsPageView:
    def __init__(self, root):
        self.root = root
        self.panel = tk.Frame(self.root, bg="white", height=550)
        self.panel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.extra = tk.Frame(self.panel, bg="white", height=50)
        self.extra.pack()
        nombres = [
            "ACARAPIA APAZA DEISY",
            "AJNOTA CAHUAYA CRISTHIAN",
            "ANDREÉ SANCHEZ MARCO ANTONIO",
            "GOMEZ NINA JHOSELIN",
            "HILARI QUENTA JOSE ALFREDO",
            "LAURA CATACORA JHONATAN JOEL",
            "PAUCARA ROMERO RODRIGO VIDAL",
            "TUSCO TALLACAGUA MIRIAM"
        ]

        for nombre in nombres:
            label = tk.Label(self.panel,
                             text=nombre,
                             bg="gray",
                             foreground="white",
                             font=("Times New Roman", 12, "bold italic"),
                             width=50,
                             pady=5,
                             borderwidth=2,
                             relief="groove")
            label.pack(side=tk.TOP, pady=10)
