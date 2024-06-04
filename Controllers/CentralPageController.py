from Views.AboutUsPageView import AboutUsPageView
from Views.ActsConditionsPageView import ActsConditionsPageView
from Views.CostsProjectionPageView import CostsProjectionPageView
from Views.GraphsPageView import GraphsPageView


class CentralPageController:
    def __init__(self, view, pageOption):
        self.view = view
        self.option = pageOption
        page_methods = {
            1: self.changeToPage1,
            2: self.changeToPage2,
            3: self.changeToPage3,
            4: self.changeToPage4,
        }

        if self.option in page_methods:
            page_methods[self.option]()

    def changeToPage1(self):
        self.option = 1
        self.view.reborn()
        ActsConditionsPageView(self.view.getPanel())

    def changeToPage2(self):
        self.option = 2
        self.view.reborn()
        view = CostsProjectionPageView(self.view.getPanel())


    def changeToPage3(self):
        self.option = 3
        self.view.reborn()
        GraphsPageView(self.view.getPanel())

    def changeToPage4(self):
        self.option = 4
        self.view.reborn()
        AboutUsPageView(self.view.getPanel())

    def addButtons(self):
        button_data = [
            ("Actos y Condiciones inseguras", self.changeToPage1),
            ("Costos Proyectados por Accidentes", self.changeToPage2),
            ("Gráficos", self.changeToPage3),
            ("Sobre nosotros", self.changeToPage4)
        ]
        self.view.addButtons(button_data)
