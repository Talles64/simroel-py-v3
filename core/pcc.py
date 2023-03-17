import numpy as np


class PathComputationClient:
    def __init__(self, node, params):
        self.node = node

        self.pcc_holding_time = params.get_pcc_holding_time()
        self.current_time = 0
        self.queue_connections = []
        self.in_transmission = []

    def get_pcc_index(self, node, pccs):
        nodes = np.array([pcc.node for pcc in pccs])
        return np.argwhere(node == nodes).flatten()[0]

    def remove_connection(self, conn):
        if conn in self.in_transmission:
            self.in_transmission.remove(conn)
        return

    def get_connection(self, conn):
        if conn in self.in_transmission:
            return self.in_transmission[self.in_transmission.index(conn)]
        return

    def add_in_transmission(self, conn):
        self.in_transmission.append(conn)

    def add_connection(self, conn):
        self.queue_connections.append(conn)

    def get_n_conn(self):
        return len(self.queue_connections)

    def clear_queue(self):
        self.queue_connections.clear()
