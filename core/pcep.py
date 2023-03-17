class PathComputationElement(object):
    def __init__(self, pccs):
        self.pc_req = []
        self.conn_list = []
        self.pccs = pccs

    def add_conn_list(self, pcc_conn_list):
        self.conn_list.extend(pcc_conn_list)

    def add_conn_assigned(self, conn):
        source = conn.src
        pcc_idx = self.pccs[0].get_pcc_index(source, self.pccs)
        self.pccs[pcc_idx].add_in_transmission(conn)

    def remove_conn_assigned(self, conn):
        source = conn.src
        pcc_idx = self.pccs[0].get_pcc_index(source, self.pccs)
        self.pccs[pcc_idx].remove_connection(conn)
