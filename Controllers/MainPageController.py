import tkinter as tk

from Controllers.CentralPageController import CentralPageController
from Views.CentralPageView import CentralPageView


class MainPageController:
    def __init__(self, view):
        self.view = view

    def changeToPage1(self):
        self.changePage(1)

    def changeToPage2(self):
        self.changePage(2)

    def changeToPage3(self):
        self.changePage(3)

    def changeToPage4(self):
        self.changePage(4)

    def changePage(self, option):
        root = self.view.getRoot()
        root.destroy()
        root = tk.Tk()
        view = CentralPageView(root)
        controller = CentralPageController(view, option)
        controller.addButtons()
        root.mainloop()

    def buttons(self):
        self.view.addButton("1. Actos y Condiciones inseguras", self.changeToPage1)
        self.view.addButton("2. Costos Proyectados por Accidentes", self.changeToPage2)
        self.view.addButton("3. Gráficos", self.changeToPage3)
        self.view.addButton("4. Sobre nosotros", self.changeToPage4)
