import tkinter as tk
from io import BytesIO
from tkinter import ttk

import numpy as np
import pandas as pd
from PIL import Image
from PIL import ImageTk
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


class CostsProjectionPageView:
    def __init__(self, root):
        self.selected_year = None
        self.n = None
        self.root = root
        self.panel = tk.Frame(self.root, bg="green", height=550)
        self.panel.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.image_label = tk.Label(self.root, bg="white", width=900, height=500)
        self.image_label.pack(pady=20)
        self.createMenu()

    def createMenu(self):
        subpanel = tk.Frame(self.panel, bg="green", height=50)
        subpanel.pack(side=tk.BOTTOM, fill=tk.BOTH)
        ttk.Label(subpanel, text="Year :", font=("Times New Roman", 10)).grid(column=0, row=15, padx=10, pady=25)

        self.n = tk.StringVar()
        monthchoosen = ttk.Combobox(subpanel, width=5, textvariable=self.n)

        monthchoosen['values'] = (
            '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019',
            '2020', '2021', '2022')

        monthchoosen.grid(column=1, row=15)
        monthchoosen.current(1)
        monthchoosen.bind("<<ComboboxSelected>>", self.onYearSelect)

    def onYearSelect(self, event):
        self.selected_year = self.n.get()
        print("Selected year:", self.selected_year)
        self.generate_graph(int(self.selected_year) - 2006)

    def generate_graph(self, year):
        csv_filename = f'Static/CostoxAccidenteT1.csv'
        df = pd.read_csv(csv_filename)

        years = df.iloc[1:, 0]
        print(years.get(year))

        costoT1 = df.iloc[1:, 1]
        frecuenciaT1 = df.iloc[1:, 2]
        print(costoT1.get(year))
        print(frecuenciaT1.get(year))

        costoT2 = df.iloc[1:, 3]
        frecuenciaT2 = df.iloc[1:, 4]
        print(costoT2.get(year))
        print(frecuenciaT2.get(year))

        costoT3 = df.iloc[1:, 5]
        frecuenciaT3 = df.iloc[1:, 6]
        print(costoT3.get(year))
        print(frecuenciaT3.get(year))

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

        # Crear gráfico de dispersión para y2
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
