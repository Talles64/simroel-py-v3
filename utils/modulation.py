""" TODO
TESTAR SE AS CONTAS BATEM
"""


import numpy as np

SPECTRAL_EFFS = {
    "4-QAM": 4,
    "8-QAM": 8,
    "16-QAM": 16,
    "32-QAM": 32,
    "64-QAM": 64
}


class Modulation:
    def __init__(self, params):
        self.guard_band = params.get_guard_band()
        self.slot_size = params.get_slot_size()
        self.modulations = params.get_modulation()
        self.lim_single_carrier = params.get_limit_single_carrier()
        self.spectral_eff = 0.0

        self.b_super_channel = dict(zip(self.modulations, [0.0, 0.0, 0.081, 0.045, 0.0]))

    def calculate_n_slots(self, modulation, conn):
        self.set_spectral_eff(modulation)

        if conn.size <= self.lim_single_carrier: return self.single_carrier(conn)
        return int(self.super_channel(modulation, conn))

    def single_carrier(self, conn):
        slots = np.ceil(conn.size / (self.slot_size * self.spectral_eff))
        return slots + self.guard_band

    def super_channel(self, modulation, conn):
        nsc = np.ceil(conn.size / self.lim_single_carrier)
        rs = self.lim_single_carrier / self.spectral_eff
        size = ((nsc - 1) * (1 + self.b_super_channel.get(modulation)) + 1) * rs
        slots = np.ceil(size / self.slot_size)
        return slots + self.guard_band

    def set_spectral_eff(self, modulation):
        eff = SPECTRAL_EFFS.get(modulation, 2)
        self.spectral_eff = 2 * (np.log10(eff) / np.log10(2))
        return
