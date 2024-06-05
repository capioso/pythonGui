import tkinter as tk

from Controllers.MainPageController import MainPageController
from Views.MainPageView import MainPageView

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    mainview = MainPageView(root)
    maincontroller = MainPageController(mainview)
    maincontroller.buttons()
    root.mainloop()
