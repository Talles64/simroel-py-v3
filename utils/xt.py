import pandas as pd
import numpy as np

import math
def hascrosstalk(core, slot, mcf):
    Xt = []
    for cores in MCF_7["adjs"][core]:
        if alocationtabble[cores][slot] == 1:
            Xt.append(cores)

        else:
            pass
    if Xt == []:
        return False
    else:
        return Xt

def CalculateCrosstalk(x,k,b,r,d,l, alocate):
    if hascrosstalk(corea, slota, MCF_7) == False:
        print("não tem XT")
        pass
    else:
        xt = 2*((math.pow(k,2)/b)*(r/d))*l
        if alocate == True:
            for core in x:
                xtabble[core]+=xt
                print(f"no core {core} o Xt é igual a {xtabble[core]}")
            xtabble[corea]+=xt
            print(f"no core {corea} o Xt é igual a {xtabble[corea]}")
        else:
            for core in x:
                xtabble[core]-=xt
                print(f"no core {core} o Xt é igual a {xtabble[core]}")
            xtabble[corea]-=xt
            print(f"no core {corea} o Xt é igual a {xtabble[corea]}")