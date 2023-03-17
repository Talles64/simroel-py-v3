import numpy as np


class Fiber(object):
    def __init__(self, params):
        self.cores = params.get_n_cores()
        self.slot_size = params.get_slot_size()
        self.bandwidth = params.get_bandwidth()
        self.n_slots = np.ceil(self.bandwidth / self.slot_size).astype(int)

        src_tgt = params.get_topology()[1]
        data = [np.full((self.cores, self.n_slots), -1, dtype=np.int8)
                for _ in range(len(src_tgt))]

        self.fiber_data = dict(zip(src_tgt, data))

    def alloc(self, conn):
        for pair in conn.route:
            self.fiber_data.get(pair)[conn.fiber_core, conn.free_slots[0]:conn.free_slots[1]] = 0
            self.fiber_data.get(pair)[conn.fiber_core, conn.free_slots[1] - 1] = -2
        return

    def free(self, conn):
        for pair in conn.route:
            self.fiber_data.get(pair)[conn.fiber_core, conn.free_slots[0]:conn.free_slots[1]] = -1