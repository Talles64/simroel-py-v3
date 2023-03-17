import pandas as pd
import numpy as np
from files.file_manager import FileManager


class ConfidenceInterval:
    def __init__(self):
        fm = FileManager()
        ci_path = fm.confidence_interval_path

        self.ci = fm.get_properties()["ci"]
        self.n_sims = fm.get_properties()["simulations"]
        self.data = pd.read_csv(ci_path).set_index("index")

    def get_interval(self):
        percentage = self.percentage()
        n_simulations = self.n_simulations()

        indices = {
            40: self.data.loc["31", self.i] if percentage else -1,
            60: self.data.loc["32", self.i] if percentage else -1,
            120: self.data.loc["33", self.i] if percentage else -1
        }

        if self.n_sims <= 30:
            return self.data.iloc[self.j, self.i] if (percentage and n_simulations) else -1

        return indices.get(self.n_sims, self.data.loc["34", self.i] if percentage else -1)

    def percentage(self):
        condition = self.data.columns == str(self.ci)
        percentage = np.any(condition)
        self.i = self.data.columns[condition][0] if percentage else self.data.columns[-1]
        return percentage

    def n_simulations(self):
        condition = self.data.index == str(self.n_sims)
        sims = np.any(condition)
        self.j = self.data.index[condition][0] if sims else self.data.index[-1]
        return sims
