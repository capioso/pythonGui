import tkinter as tk
from io import BytesIO

from PIL import Image
from PIL import ImageTk
from matplotlib import pyplot as plt, ticker
from matplotlib.backends.backend_agg import FigureCanvasAgg

from Services.AccidenteGlobal import AccidenteGlobal


class CostsProjectionPageView:

    def __init__(self, root):
        self.globalData = AccidenteGlobal()
        self.x = self.globalData.getYear()
        self.x = list(map(int, self.x))
        self.y1 = self.globalData.getT1()
        self.y2 = self.globalData.getT2()
        self.y3 = self.globalData.getT3()
        self.costsT1 = self.globalData.getCostT1()
        self.costsT2 = self.globalData.getCostT2()
        self.costsT3 = self.globalData.getCostT3()
        self.costsT4 = self.globalData.getCosts()

        self.root = root
        self.panel = tk.Frame(self.root, bg="white")
        self.panel.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=10)
        self.canvas = tk.Canvas(self.panel, bg="white", height=500)
        self.scroll_y = tk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)
        self.canvas.pack(side=tk.TOP, fill="both", expand=True)
        self.scroll_y.pack(side=tk.RIGHT, fill="y")
        self.image_label = tk.Label(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.image_label, anchor="nw")
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.button = tk.Button(self.panel,
                                bg="gray",
                                foreground="white",
                                width=20,
                                text="Cost Prediction",
                                font=("Times new roman", 12, "bold"),
                                command=self.grapher)
        self.button.pack(side=tk.LEFT, padx=10, pady=5)
        self.grapher()
        self.canvas.move("all", 325, 5)

    def grapher(self):
        self.x = self.globalData.getYear()
        self.x = list(map(int, self.x))
        self.y1 = self.globalData.getT1()
        self.y2 = self.globalData.getT2()
        self.y3 = self.globalData.getT3()
        self.costsT1 = self.globalData.getCostT1()
        self.costsT2 = self.globalData.getCostT2()
        self.costsT3 = self.globalData.getCostT3()
        self.costsT4 = self.globalData.getCosts()

        fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(8, 14))

        ax1.plot(self.x, self.y1, label='TAT1', color='blue')
        ax1.set_ylabel('TAT1')
        ax1.set_title('Frecuencia y Costo de accidentes tipo 1', pad=55, fontname="Times New Roman", fontweight='bold',
                      fontsize=16)
        ax1.legend()
        ax1.grid(True)

        ax2.plot(self.x, self.y2, label='TAT2', color='red')
        ax2.set_ylabel('TAT2')
        ax2.set_title('Frecuencia y Costo de accidentes tipo 2', pad=55, fontname="Times New Roman", fontweight='bold',
                      fontsize=16)
        ax2.legend()
        ax2.grid(True)

        ax3.plot(self.x, self.y3, label='TAT3', color='magenta')
        ax3.set_ylabel('TAT3')
        ax3.set_title('Frecuencia y Costo de accidentes tipo 3', pad=55, fontname="Times New Roman", fontweight='bold',
                      fontsize=16)
        ax3.legend()
        ax3.grid(True)

        ax4.plot(self.x, self.costsT4, label='Costo', color='brown')
        ax4.set_ylabel('Costo')
        ax4.set_title('Costo por año', pad=55, fontname="Times New Roman", fontweight='bold',
                      fontsize=16)
        ax4.legend()
        ax4.grid(True)

        ax1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:.0f}'.format(x)))
        ax2.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:.0f}'.format(x)))
        ax3.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:.0f}'.format(x)))
        ax4.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:.0f}'.format(x)))

        for xi in self.x:
            ax1.axvline(xi, color='gray', linestyle='--', linewidth=0.5)
            ax2.axvline(xi, color='gray', linestyle='--', linewidth=0.5)
            ax3.axvline(xi, color='gray', linestyle='--', linewidth=0.5)
            ax4.axvline(xi, color='gray', linestyle='--', linewidth=0.5)

        ax1.set_xticks(self.x)
        ax1.set_xticklabels(self.x, rotation=45)
        ax2.set_xticks(self.x)
        ax2.set_xticklabels(self.x, rotation=45)
        ax3.set_xticks(self.x)
        ax3.set_xticklabels(self.x, rotation=45)
        ax4.set_xticks(self.x)
        ax4.set_xticklabels(self.x, rotation=45)

        for xi, cost in zip(self.x, self.costsT1):
            formatted_cost = format(cost, '.2f')
            ax1.annotate(f'{formatted_cost}', (xi, max(self.y1) * 1.2), textcoords="offset points", xytext=(0, 10),
                         ha=tk.LEFT, fontsize=8, rotation=45)

        for xi, cost in zip(self.x, self.y1):
            ax1.annotate(f'{cost}', (xi, self.y1[self.x.index(xi)]), textcoords="offset points", xytext=(0, 10),
                         ha=tk.CENTER, fontsize=8, fontweight='bold')

        for xi, cost in zip(self.x, self.costsT2):
            formatted_cost = format(cost, '.2f')
            ax2.annotate(f'{formatted_cost}', (xi, max(self.y2) * 1.2), textcoords="offset points", xytext=(0, 10),
                         ha=tk.LEFT, fontsize=8, rotation=45)

        for xi, cost in zip(self.x, self.y2):
            ax2.annotate(f'{cost}', (xi, self.y2[self.x.index(xi)]), textcoords="offset points", xytext=(0, 10),
                         ha=tk.CENTER, fontsize=8, fontweight='bold')

        for xi, cost in zip(self.x, self.costsT3):
            formatted_cost = format(cost, '.2f')
            ax3.annotate(f'{formatted_cost}', (xi, max(self.y3) * 1.2), textcoords="offset points", xytext=(0, 10),
                         ha=tk.LEFT, fontsize=8, rotation=45)

        for xi, cost in zip(self.x, self.y3):
            ax3.annotate(f'{cost}', (xi, self.y3[self.x.index(xi)]), textcoords="offset points", xytext=(0, 10),
                         ha=tk.CENTER, fontsize=8, fontweight='bold')

        for xi, cost in zip(self.x, self.costsT4):
            formatted_cost = format(cost, '.2f')
            ax4.annotate(f'{formatted_cost}', (xi, max(self.costsT4) * 1.2), textcoords="offset points", xytext=(0, 10),
                         ha=tk.LEFT, fontsize=8, rotation=45)

        ax1.set_ylim(top=max(self.y1) * 1.2)
        ax2.set_ylim(top=max(self.y2) * 1.2)
        ax3.set_ylim(top=max(self.y3) * 1.2)
        ax4.set_ylim(top=max(self.costsT4) * 1.2)

        plt.tight_layout()
        plt.subplots_adjust(hspace=1.0)

        canvas = FigureCanvasAgg(fig)
        canvas.draw()
        buffer = BytesIO()
        canvas.print_png(buffer)
        buffer.seek(0)
        image = Image.open(buffer)
        width, height = image.size
        max_height = height
        max_width = 800
        resized_image = image.resize((max_width, max_height))
        graph_image = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=graph_image)
        self.image_label.image = graph_image
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.globalData.train()
