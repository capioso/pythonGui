import tkinter as tk
from io import BytesIO
from tkinter import ttk

import pandas as pd
from PIL import Image
from PIL import ImageTk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg


class CostsProjectionPageView:
    dataset = pd.read_csv(f'Static/CostoxAccidenteT1.csv')

    def __init__(self, root):
        self.selected_year = None
        self.n = None
        self.years = CostsProjectionPageView.dataset.iloc[1:, 0]
        self.root = root
        self.panel = tk.Frame(self.root, bg="white", height=550)
        self.panel.pack(side=tk.BOTTOM, fill=tk.BOTH)

        self.image_label = tk.Label(self.root, bg="white", width=900, height=500)
        self.image_label.pack(pady=20)
        self.createMenu()

    def createMenu(self):
        subpanel = tk.Frame(self.panel, bg="white", height=50)
        subpanel.pack(side=tk.BOTTOM, fill=tk.BOTH)
        (ttk.Label(subpanel,
                   text="Year",
                   font=("Times New Roman", 14, "bold"),
                   padding=10,
                   background="white")
         .grid(column=0, row=15, padx=10, pady=25))

        self.n = tk.StringVar()
        yearPicker = ttk.Combobox(subpanel,
                                   width=10,
                                   justify="center",
                                   height=10,
                                   textvariable=self.n,
                                   state="readonly",
                                   background="white",
                                   foreground="black",
                                   font=("Times New Roman", 12, "bold"))
        yearPicker['values'] = sorted(set(int(year) for year in self.years))
        yearPicker.grid(column=1, row=15)
        yearPicker.bind("<<ComboboxSelected>>", self.onYearSelect)

    def onYearSelect(self, event):
        self.selected_year = self.n.get()
        self.generate_graph(int(self.selected_year) - 2006)

    def generate_graph(self, year):
        costoT1 = CostsProjectionPageView.dataset.iloc[1:, 1]
        frecuenciaT1 = CostsProjectionPageView.dataset.iloc[1:, 2]

        costoT2 = CostsProjectionPageView.dataset.iloc[1:, 3]
        frecuenciaT2 = CostsProjectionPageView.dataset.iloc[1:, 4]

        costoT3 = CostsProjectionPageView.dataset.iloc[1:, 5]
        frecuenciaT3 = CostsProjectionPageView.dataset.iloc[1:, 6]

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))
        x = ["T1", "T2", "T3"]
        y1 = [float(costoT1.get(year).replace(",", ".")), float(costoT2.get(year).replace(",", ".")),
              float(costoT3.get(year).replace(",", "."))]
        y2 = [float(frecuenciaT1.get(year).replace(",", ".")), float(frecuenciaT2.get(year).replace(",", ".")),
              float(frecuenciaT3.get(year).replace(",", "."))]

        ax1.plot(x, y1, 'g-', marker='o')
        ax1.set_ylabel('Costo', color='g')
        ax1.set_title('Costo y Frecuencia en el año {}'.format(year + 2006))

        ax2.plot(x, y2, 'b-', marker='o')
        ax2.set_xlabel('X Label')
        ax2.set_ylabel('Frecuencia', color='b')

        for x_val, y_val in zip(x, y1):
            ax1.scatter(x_val, y_val, color='g')
            ax1.text(x_val, y_val, str(y_val), ha='center', va='bottom')

        for x_val, y_val in zip(x, y2):
            ax2.scatter(x_val, y_val, color='b')
            ax2.text(x_val, y_val, str(y_val), ha='center', va='bottom')

        plt.tight_layout()

        canvas = FigureCanvasAgg(fig)
        canvas.draw()

        buffer = BytesIO()
        canvas.print_png(buffer)
        buffer.seek(0)
        image = Image.open(buffer)

        width, height = image.size
        aspect_ratio = width / height

        max_height = 400
        max_width = int(max_height * aspect_ratio)
        resized_image = image.resize((max_width, max_height), Image.FIXED)

        graph_image = ImageTk.PhotoImage(resized_image)
        self.image_label.config(image=graph_image)
        self.image_label.image = graph_image
