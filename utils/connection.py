from collections import Counter
import numpy as np
from dataclasses import dataclass, field
from typing import List, Any


@dataclass(repr=True)
class Connection(object):
    iid: int
    src: int
    tgt: int
    size: int
    hold: float
    arrive: float
    params: Any
    slots: int = -1
    release: float = 0.0
    fiber_core: int = -1
    fiber_slot: int = -1
    route: List[int] = field(default_factory=list)
    id_src: int = -1
    id_tgt: int = -1
    modulation: str = ""
    power: float = 0.0
    sim_clock: float = -1.0
    fiber_cross: Any = None
    free_slots: List[int] = field(default_factory=list)

    def __post_init__(self):
        self.mcf_fiber_config = self.params.get_mcf_config()
        self.guard_band = self.params.get_guard_band()

    def __eq__(self, other):
        return self.iid == other.iid