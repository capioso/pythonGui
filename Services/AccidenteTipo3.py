import pandas as pd


class AccidenteTipo3:

    def __init__(self, year):
        self.year = int(year) - 2005
        self.dataset = pd.read_csv(f'Static/Cantidad_Accidentes_Tipo_3.csv')

        self.cols = self.dataset.iloc[self.year, 1:]
        self.cols = self.cols.tolist()
        self.cols = [self.cols[i:i + 5] for i in range(0, len(self.cols), 5)]

    def getCols(self):
        return self.cols
