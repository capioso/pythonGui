import tkinter as tk
from io import BytesIO
from tkinter import ttk

import pandas as pd
from PIL import ImageTk
from PIL import Image
from matplotlib import pyplot as plt, ticker
from matplotlib.backends.backend_agg import FigureCanvasAgg

from Models.AccidenteGlobal import AccidenteGlobal
from Models.AccidenteTipo1 import AccidenteTipo1
from Models.AccidenteTipo2 import AccidenteTipo2
from Models.AccidenteTipo3 import AccidenteTipo3


class GraphsPageView:
    def __init__(self, root):
        self.yearSelected = None
        self.dataset = None
        self.subpanel = None
        self.typeSelected = None
        self.globalData = AccidenteGlobal()
        self.root = root
        self.panel = tk.Frame(self.root, bg="white", height=550)
        self.panel.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=10)
        self.createMenu()

        self.canvas = tk.Canvas(self.panel, bg="white")
        self.scroll_y = tk.Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scroll_y.set)

        self.canvas.pack(side=tk.TOP, fill="both", expand=True)
        self.scroll_y.pack(side=tk.RIGHT, fill="y")
        self.image_label = tk.Label(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.image_label, anchor="nw")
        self.canvas.move("all", 325, 5)
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )
        self.isFirstType = True
        self.isFirstYear = True

    def createMenu(self):
        self.subpanel = tk.Frame(self.panel, bg="white", height=50)
        self.subpanel.pack(side=tk.BOTTOM, fill=tk.BOTH)
        button = tk.Button(self.subpanel,
                           text="Global Prediction",
                           command=self.globalPrediction,
                           width=20,
                           font=("Calibri", 12, "bold"),
                           background='gray',
                           foreground='white',
                           highlightbackground='black')
        button.pack(side=tk.LEFT, fill=tk.BOTH)
        title_label = ttk.Label(self.subpanel,
                                text="Cantidad de accidentes",
                                font=("Times New Roman", 14, "bold"),
                                background="white")
        title_label.pack(side=tk.LEFT, padx=10, pady=25)

        self.typeSelected = tk.StringVar()
        typePicker = ttk.Combobox(self.subpanel,
                                  width=10,
                                  justify="center",
                                  height=10,
                                  textvariable=self.typeSelected,
                                  state="readonly",
                                  background="white",
                                  foreground="black",
                                  font=("Times New Roman", 12, "bold"),
                                  values=["Tipo 1", "Tipo 2", "Tipo 3"])
        typePicker.pack(side=tk.LEFT)
        typePicker.bind("<<ComboboxSelected>>", self.onTypeSelected)

    def onTypeSelected(self, event):
        if self.typeSelected.get() == "Tipo 1":
            self.dataset = pd.read_csv(f'Static/Cantidad_Accidentes_Tipo_1.csv')
        if self.typeSelected.get() == "Tipo 2":
            self.dataset = pd.read_csv(f'Static/Cantidad_Accidentes_Tipo_2.csv')
        if self.typeSelected.get() == "Tipo 3":
            self.dataset = pd.read_csv(f'Static/Cantidad_Accidentes_Tipo_3.csv')

        years = self.dataset.iloc[2:, 0]
        years = [int(year) for year in years.tolist()]

        if self.isFirstType:
            subpanel = tk.Frame(self.subpanel, bg="white", height=50)
            subpanel.pack(side=tk.BOTTOM, fill=tk.BOTH)
            title_label = ttk.Label(subpanel,
                                    text="Year",
                                    font=("Times New Roman", 14, "bold"),
                                    background="white")
            title_label.pack(side=tk.LEFT, padx=10, pady=25)

            self.yearSelected = tk.StringVar()
            yearPicker = ttk.Combobox(subpanel,
                                      width=10,
                                      justify="center",
                                      height=10,
                                      textvariable=self.yearSelected,
                                      state="readonly",
                                      background="white",
                                      foreground="black",
                                      font=("Times New Roman", 12, "bold"),
                                      values=years)
            yearPicker.pack(side=tk.LEFT)
            yearPicker.bind("<<ComboboxSelected>>", self.onYearSelected)
            self.isFirstType = False
        else:
            self.grapher()

    def onYearSelected(self, event):
        self.grapher()

    def grapher(self):
        if self.typeSelected.get() == "Tipo 1":
            base = AccidenteTipo1(self.yearSelected.get())
            dividedList = base.getCols()
            y1 = [int(subList[0]) for subList in dividedList]
            y2 = [int(subList[1]) for subList in dividedList]
            x = ['AREA 1', 'AREA 2', 'AREA 3', 'AREA 4', 'AREA 5', 'AREA 6']
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

            ax1.plot(x, y1, label='Contusión', color='blue')
            ax1.set_ylabel('Contusión')
            ax1.legend()
            ax1.grid(True)

            ax2.plot(x, y2, label='Cortadura', color='red')
            ax2.set_ylabel('Cortadura')
            ax2.legend()
            ax2.grid(True)

            plt.tight_layout()
        if self.typeSelected.get() == "Tipo 2":
            base = AccidenteTipo2(self.yearSelected.get())
            dividedList = base.getCols()
            y1 = [int(subList[0]) for subList in dividedList]
            y2 = [int(subList[1]) for subList in dividedList]
            y3 = [int(subList[2]) for subList in dividedList]
            y4 = [int(subList[3]) for subList in dividedList]
            y5 = [int(subList[4]) for subList in dividedList]
            y6 = [int(subList[5]) for subList in dividedList]
            y7 = [int(subList[6]) for subList in dividedList]
            x = ['AREA 1', 'AREA 2', 'AREA 3', 'AREA 4', 'AREA 5', 'AREA 6']
            fig, axs = plt.subplots(7, 1, figsize=(10, 16))

            # Flatten the array of axes
            axs = axs.flatten()

            axs[0].plot(x, y1, label='Herida punzo cortante', color='blue')
            axs[0].legend()
            axs[0].grid(True)

            axs[1].plot(x, y2, label='Fractura', color='red')
            axs[1].legend()
            axs[1].grid(True)

            axs[2].plot(x, y3, label='Luxación', color='green')
            axs[2].legend()
            axs[2].grid(True)

            axs[3].plot(x, y4, label='Lumbalgia', color='orange')
            axs[3].legend()
            axs[3].grid(True)

            axs[4].plot(x, y5, label='Traumatismo', color='purple')
            axs[4].legend()
            axs[4].grid(True)

            axs[5].plot(x, y6, label='Esguince', color='brown')
            axs[5].legend()
            axs[5].grid(True)

            axs[6].plot(x, y7, label='Tendinitis', color='pink')
            axs[6].legend()
            axs[6].grid(True)

            for i in range(7, len(axs)):
                fig.delaxes(axs[i])

            plt.tight_layout()
            plt.subplots_adjust(wspace=0.4, hspace=0.4)
        if self.typeSelected.get() == "Tipo 3":
            base = AccidenteTipo3(self.yearSelected.get())
            dividedList = base.getCols()
            y1 = [int(subList[0]) for subList in dividedList]
            y2 = [int(subList[1]) for subList in dividedList]
            y3 = [int(subList[2]) for subList in dividedList]
            y4 = [int(subList[3]) for subList in dividedList]
            y5 = [int(subList[4]) for subList in dividedList]
            x = ['AREA 1', 'AREA 2', 'AREA 3', 'AREA 4', 'AREA 5', 'AREA 6']
            fig, axs = plt.subplots(5, 1, figsize=(10, 16))

            # Flatten the array of axes
            axs = axs.flatten()

            axs[0].plot(x, y1, label='Cuerpo extraño en ojo', color='blue')
            axs[0].legend()
            axs[0].grid(True)

            axs[1].plot(x, y2, label='Quemadura', color='red')
            axs[1].legend()
            axs[1].grid(True)

            axs[2].plot(x, y3, label='Aplastamiento', color='green')
            axs[2].legend()
            axs[2].grid(True)

            axs[3].plot(x, y4, label='Amputación', color='orange')
            axs[3].legend()
            axs[3].grid(True)

            axs[4].plot(x, y5, label='Desgarro muscular', color='purple')
            axs[4].legend()
            axs[4].grid(True)

            for i in range(5, len(axs)):
                fig.delaxes(axs[i])

            plt.tight_layout()
            plt.subplots_adjust(wspace=0.4, hspace=0.4)
        self.canvasSetter(fig)

    def canvasSetter(self, figure):
        canvas = FigureCanvasAgg(figure)
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

    def globalPrediction(self):
        x = self.globalData.getYear()
        x = list(map(int, x))
        y1 = self.globalData.getT1()
        y2 = self.globalData.getT2()
        y3 = self.globalData.getT3()

        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

        ax1.plot(x, y1, label='TAT1', color='blue')
        ax1.set_ylabel('TAT1')
        ax1.legend()
        ax1.grid(True)

        ax2.plot(x, y2, label='TAT2', color='red')
        ax2.set_ylabel('TAT2')
        ax2.legend()
        ax2.grid(True)

        ax3.plot(x, y3, label='TAT3', color='red')
        ax3.set_ylabel('TAT3')
        ax3.legend()
        ax3.grid(True)

        ax1.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:.0f}'.format(x)))
        ax2.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:.0f}'.format(x)))
        ax3.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: '{:.0f}'.format(x)))

        for xi in x:
            ax1.axvline(xi, color='gray', linestyle='--', linewidth=0.5)
            ax2.axvline(xi, color='gray', linestyle='--', linewidth=0.5)
            ax3.axvline(xi, color='gray', linestyle='--', linewidth=0.5)

        ax1.set_xticks(x)
        ax1.set_xticklabels(x, rotation=45)
        ax2.set_xticks(x)
        ax2.set_xticklabels(x, rotation=45)
        ax3.set_xticks(x)
        ax3.set_xticklabels(x, rotation=45)

        plt.tight_layout()
        plt.subplots_adjust(hspace=0.5)

        self.canvasSetter(fig)
        self.globalData.train()
