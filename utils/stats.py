import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.reload_library()


from files.properties import Properties

class Statistics(object):
    def __init__(self, params:Properties):
        self.n_handled = 0
        self.n_allocted = 0

        self.b_resource = 0
        self.b_osnr = 0
        self.b_crosstalk = 0

        self.stats = pd.DataFrame(np.zeros(4).reshape(1, 4),
                                  columns=['numConnections', 'blockedByResources', 'blockedByOSNR',
                                           'blockedByCrosstalk'])
        self.data = pd.DataFrame(np.zeros(2).reshape(1, 2),
                                 columns=['lambda', 'blocked'])
        self.lambda_nw = params.get_traffic_lambda()

    def allocated(self):
        self.n_allocted += 1
        aux = pd.DataFrame(np.array(
            [self.stats.iloc[-1]['numConnections'] + 1, self.stats.iloc[-1]['blockedByResources'],
             self.stats.iloc[-1]['blockedByOSNR'], self.stats.iloc[-1]['blockedByCrosstalk']]).reshape(1, 4),
                           columns=['numConnections', 'blockedByResources', 'blockedByOSNR',
                                    'blockedByCrosstalk'])
        self.stats = pd.concat([self.stats, aux])

    def handled(self):
        self.n_handled += 1

    def resource(self):
        self.b_resource += 1
        aux = pd.DataFrame(
            np.array([self.stats.iloc[-1]['numConnections'] + 1, self.stats.iloc[-1]['blockedByResources'] + 1,
                      self.stats.iloc[-1]['blockedByOSNR'],
                      self.stats.iloc[-1]['blockedByCrosstalk']]).reshape(1, 4),
            columns=['numConnections', 'blockedByResources', 'blockedByOSNR', 'blockedByCrosstalk'])
        self.stats = pd.concat([self.stats, aux])

    def osnr(self):
        self.b_osnr += 1
        aux = pd.DataFrame(
            np.array([self.stats.iloc[-1]['numConnections'] + 1, self.stats.iloc[-1]['blockedByResources'],
                      self.stats.iloc[-1]['blockedByOSNR'] + 1,
                      self.stats.iloc[-1]['blockedByCrosstalk']]).reshape(1, 4),
            columns=['numConnections', 'blockedByResources', 'blockedByOSNR', 'blockedByCrosstalk'])
        self.stats = pd.concat([self.stats, aux])

    def crosstalk(self):
        self.b_crosstalk += 1
        aux = pd.DataFrame(
            np.array([self.stats.iloc[-1]['numConnections'] + 1, self.stats.iloc[-1]['blockedByResources'],
                      self.stats.iloc[-1]['blockedByOSNR'],
                      self.stats.iloc[-1]['blockedByCrosstalk'] + 1]).reshape(1, 4),
            columns=['numConnections', 'blockedByResources', 'blockedByOSNR', 'blockedByCrosstalk'])
        self.stats = pd.concat([self.stats, aux])

    def block_control(self, alloc_status):
        if alloc_status == "resource":
            self.resource()
            return False
        elif alloc_status == "osnr":
            self.osnr()
            return False
        elif alloc_status == "crosstalk":
            self.crosstalk()
            return False
        elif alloc_status == "allocated":
            self.allocated()
            return True
        else:
            raise ValueError("alloc_status must be 'resource', 'osnr', 'crosstalk' or 'allocated'")

    def summarize(self):
        text = f"""
           [*] Total connections handled: {self.n_handled}
           [*] Total connections allocated: {self.n_allocted} ({(self.n_allocted / self.n_handled) * 100:.2f}%)
           ********* BLOCKED (+) *********
           [-] Resource: {self.b_resource} ({(self.b_resource / self.n_handled) * 100:.4f}%)
           [-] OSNR: {self.b_osnr} ({(self.b_osnr / self.n_handled) * 100:.4f}%)
           [-] XT: {self.b_crosstalk} ({(self.b_crosstalk / self.n_handled) * 100:.4f}%)
           ********** DEBUG (+) **********
           [+] Total: {self.b_resource + self.b_osnr + self.b_crosstalk + self.n_allocted}
           """
        print(text)

    def plot(self):
        fig = plt.plot(figsize=(15, 20), constrained_layout=True)
        plt.xlabel('numConnections', fontsize=11)
        plt.ylabel('Probabilidade de Bloqueio', fontsize=11)
        plt.grid()
        self.stats['blockedByResources'] = self.stats['blockedByResources'] / self.n_handled
        self.stats.plot(x='numConnections', y='blockedByResources')
        plt.savefig('blockedByResources.png')

    def get_data(self):
        block_probability = (self.b_resource + self.b_osnr + self.b_crosstalk) / self.n_handled

        aux = pd.DataFrame(np.array([1 / self.lambda_nw, block_probability]).reshape(1, 2),
                           columns=['lambda', 'blocked'])
        return aux

    def convert_value(value: str) -> float:
        if 'E' in value:
            number = value.split('E')
            return float(number[0]) * (10 ** int(number[1]))
        return float(value)

    def plot_lambda(self, data):
        data  = data.drop(0)
        data = data.groupby('lambda').mean()
        fig, ax = plt.subplots()
        ax.set_xticks(data.index)
        ax.set_yscale('log')
        ax.set_xlabel('Carga (Erlang)', fontsize=11)
        ax.set_ylabel('Probabilidade de Bloqueio', fontsize=11)
        ax.grid()
        ax.plot(data.index, data['blocked'], color='red', marker='o', label='Bloqueio')
        print('*' * 30)
        print(data)
        fig.show()
        fig.savefig('plot.png')