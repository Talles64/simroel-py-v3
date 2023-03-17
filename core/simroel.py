from simulation import Simulation
import json
from utils.stats import Statistics
from files.properties import Properties
import pandas as pd
import numpy as np
data_simulation = pd.DataFrame(np.zeros(2).reshape(1, 2),columns=['lambda', 'blocked'])

for erlang in [1200, 1300, 1400]:
    with open('../data/parameters.json', 'r+') as f:
        data = json.load(f)
        data['traffic_lambda'] = 1/erlang # <--- add id value.
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part
    for i in range(1):
        sim = Simulation()
        sim.simulate()
        sim.stats.summarize()
        aux = sim.stats.get_data()
        data_simulation = pd.concat([data_simulation, aux])
        print(erlang)
print(data_simulation)
sim.stats.plot_lambda(data_simulation)
