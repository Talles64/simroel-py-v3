import numpy as np
from operator import itemgetter


class Assignment(object):
    def __init__(self, allocation_type):
        assert allocation_type in ["first_fit", "random_fit"], "Accepted allocation types: [first_fit, random_fit]"
        self.allocation_type = allocation_type

    def set_allocation_type(self, allocation_type):
        self.allocation_type = allocation_type

    def first_fit(self, conn, fiber, route, core):
        """ fiber: Fiber(object).fiber """

        sample = np.stack(itemgetter(*route)(fiber))
        if len(route) == 1:
            sample = np.expand_dims(sample, 0)

        slot_size = int(conn.slots)
        guard_band = conn.guard_band
        for slot in range(sample.shape[-1] - 1 - slot_size+guard_band):
            if np.all((sample[:, core, slot:slot+slot_size+guard_band]) == -1):
                return slot, slot+slot_size+guard_band
        return -1

    def random_fit(self, conn, fiber, route, core):
        """ fiber: Fiber(object).fiber """

        sample = np.stack(itemgetter(*route)(fiber))
        if len(route) == 1:
            sample = np.expand_dims(sample, 0)

        fiber_slots = []
        slot_size = int(conn.slots)
        guard_band = conn.guard_band

        for slot in range(sample.shape[-1] - 1 - slot_size+guard_band):
            if np.all((sample[:, core, slot:slot+slot_size+guard_band]) == -1):
                fiber_slots.append((slot, slot+slot_size+guard_band))

        if len(fiber_slots) == 0: return -1
        np.random.shuffle(fiber_slots)
        return fiber_slots[0]

    def alloc(self, conn, fiber, route, core):
        free_slots = getattr(self, self.allocation_type)(conn, fiber.fiber_data, route, core)
        if free_slots == -1: return False

        conn.fiber_core = core
        conn.fiber_slot = free_slots[0]
        conn.free_slots = free_slots
        conn.route = route

        fiber.alloc(conn)
        return True
    