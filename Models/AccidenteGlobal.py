import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


class AccidenteGlobal:

    def __init__(self):
        self.dataset = pd.read_csv(f'Static/Global.csv')

        self.year = self.dataset.iloc[0:, 0]
        self.year = self.year.tolist()
        self.t1 = self.dataset.iloc[0:, 1]
        self.t1 = self.t1.tolist()
        self.t2 = self.dataset.iloc[0:, 2]
        self.t2 = self.t2.tolist()
        self.t3 = self.dataset.iloc[0:, 3]
        self.t3 = self.t3.tolist()

    def getYear(self):
        return self.year

    def getT1(self):
        return self.t1

    def getT2(self):
        return self.t2

    def getT3(self):
        return self.t3

    def train(self):
        last = self.year[-1]
        self.year.append(last + 1)

        tat1_model = ARIMA(self.t1, order=(6, 1, 0))
        tat1_fit = tat1_model.fit()
        self.t1.append(int(tat1_fit.forecast(steps=1)[0]))

        tat2_model = ARIMA(self.t2, order=(5, 1, 0))
        tat2_fit = tat2_model.fit()
        self.t2.append(int(tat2_fit.forecast(steps=1)[0]))

        tat3_model = ARIMA(self.t3, order=(5, 1, 0))
        tat3_fit = tat3_model.fit()
        self.t3.append(int(tat3_fit.forecast(steps=1)[0]))
