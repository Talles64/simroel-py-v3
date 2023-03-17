import numpy as np
import math


class Crosstalk:

    def __init__(self, params):
        self.coupling_coeff = 1.2 * (math.pow(10, -2))
        self.propagation_const = math.pow(10, 7)
        self.bending_radius = params.get_bending_radius()
        self.core_pitch = params.get_core_pitch() * math.pow(10, -5)

    def hascrosstalk(self, core, slot, conn_size, routes, mcf, fiber):
        for route in routes:
            alocationtabble = fiber[route]
            Xt = dict()
            slot_alloc = list(range(slot, slot + conn_size))
            for core_adj in mcf["adjs"][core]:
                slot_adj = []
                for slot in slot_alloc:
                    if alocationtabble[core_adj][slot] == 1:
                        slot_adj.append(slot)
                        Xt.update({core_adj: slot_adj})
                        # Xt.append(core_adj)
                        # Xt.append(core)
                    else:
                        pass
            if Xt == {}:
                return False
            else:
                return Xt

    def CalculateCrosstalk(self, xt_tabble, cores_dict, allocate, conn_size, l):
        xt = 2 * ((math.pow(self.coupling_coeff, 2) / self.propagation_const) * (
                    self.bending_radius / self.core_pitch)) * l
        if allocate:
            for core in cores_dict.keys():
                xt_tabble[core] += xt * (len(cores_dict[core]) / conn_size)
                print(f"no core {core} o Xt é igual a {xt_tabble[core]}")
        if not allocate:
            for core in cores_dict.keys():
                xt_tabble[core] -= xt * (len(cores_dict[core]) / conn_size)
                print(f"no core {core} o Xt é igual a {xt_tabble[core]}")
