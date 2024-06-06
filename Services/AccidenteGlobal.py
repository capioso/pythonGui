import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


class AccidenteGlobal:

    def __init__(self):
        self.dataset = pd.read_csv(f'Static/Global.csv')

        self.year = self.dataset.iloc[0:, 0]
        self.year = self.year.tolist()
        self.year2 = self.year

        self.t1 = self.dataset.iloc[0:, 1]
        self.t1 = self.t1.tolist()
        self.t2 = self.dataset.iloc[0:, 2]
        self.t2 = self.t2.tolist()
        self.t3 = self.dataset.iloc[0:, 3]
        self.t3 = self.t3.tolist()
        self.costsT1 = self.dataset.iloc[0:, 4]
        self.costsT1 = self.costsT1.tolist()
        self.costsT1 = [float(cost.replace(',', '.')) for cost in self.costsT1]

        self.costsT2 = self.dataset.iloc[0:, 5]
        self.costsT2 = self.costsT2.tolist()
        self.costsT2 = [float(cost.replace(',', '.')) for cost in self.costsT2]

        self.costsT3 = self.dataset.iloc[0:, 6]
        self.costsT3 = self.costsT3.tolist()
        self.costsT3 = [float(cost.replace(',', '.')) for cost in self.costsT3]

        self.costs = self.dataset.iloc[0:, 7]
        self.costs = self.costs.tolist()
        self.costs = [float(cost.replace(',', '.')) for cost in self.costs]

    def getYear(self):
        return self.year

    def getYear2(self):
        return self.year2

    def getT1(self):
        return self.t1

    def getT2(self):
        return self.t2

    def getT3(self):
        return self.t3

    def getCostT1(self):
        return self.costsT1

    def getCostT2(self):
        return self.costsT2

    def getCostT3(self):
        return self.costsT3

    def getCosts(self):
        return self.costs

    def train(self):
        last = self.year[-1]
        self.year.append(last + 1)

        tat1_model = ARIMA(self.t1, order=(6, 1, 0))
        tat1_fit = tat1_model.fit()
        self.t1.append(int(tat1_fit.forecast(steps=1)[0]))

        tat2_model = ARIMA(self.t2, order=(6, 1, 0))
        tat2_fit = tat2_model.fit()
        self.t2.append(int(tat2_fit.forecast(steps=1)[0]))

        tat3_model = ARIMA(self.t3, order=(6, 1, 0))
        tat3_fit = tat3_model.fit()
        self.t3.append(int(tat3_fit.forecast(steps=1)[0]))

        ctat1_model = ARIMA(self.costsT1, order=(6, 1, 0))
        ctat1_fit = ctat1_model.fit()
        self.costsT1.append(float(ctat1_fit.forecast(steps=1)[0]))

        ctat2_model = ARIMA(self.costsT2, order=(6, 1, 0))
        ctat2_fit = ctat2_model.fit()
        self.costsT2.append(float(ctat2_fit.forecast(steps=1)[0]))

        ctat3_model = ARIMA(self.costsT3, order=(6, 1, 0))
        ctat3_fit = ctat3_model.fit()
        self.costsT3.append(float(ctat3_fit.forecast(steps=1)[0]))

        globalCost = (self.t1[-1] * self.costsT1[-1]) + (self.t2[-1] * self.costsT2[-1]) + (
                    self.t3[-1] * self.costsT3[-1])
        self.costs.append(globalCost)
