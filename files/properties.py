from .file_manager import FileManager
from data.fiber_config.mcf_config import (
    MCF_2,
    MCF_7,
    MCF_12,
    MCF_19,
    MCF_22,
    MCF_30
)
import numpy as np
import pandas as pd
from random import sample
import networkx as nx

MCF_CONFIGS = {
    2: MCF_2,
    7: MCF_7,
    12: MCF_12,
    19: MCF_19,
    22: MCF_22,
    30: MCF_30,
}

CORE_SELECTION_FN = {
    "first_fit": lambda cores: np.r_[cores[1:], cores[0]],
    "random_fit": lambda cores: sample(cores.tolist(), len(cores))
}


class Properties(object):
    def __init__(self):
        self.fm = FileManager()
        self.topologies = self.fm.dict_topologies
        self.properties = self.fm.get_properties()

    def get_mcf_config(self):
        assert self.properties["n_cores"] in [2, 7, 12, 19, 22, 30]
        return MCF_CONFIGS[self.properties["n_cores"]]

    def get_topology(self):
        topology = np.loadtxt(self.topologies[self.get_file_topology()], delimiter=";")
        source_target = (topology[:, [0, 1]]).astype(int) - 1
        source_target = list(map(tuple, source_target))
        weights = topology[:, 2]

        topology = pd.DataFrame(topology, columns=["source", "target", "weight"])
        topology[["source", "target"]] = topology[["source", "target"]].astype(int) - 1  # subtract 1 to start with 0
        graph = nx.from_pandas_edgelist(topology, source="source", target="target", edge_attr="weight")
        links = np.int_((list(set(graph.nodes))))

        return graph, source_target, weights, links

    def get_traffic_input_file(self):
        return self.properties.traffic_input_file

    def get_n_connections(self):
        assert isinstance(self.properties["n_connections"], int)
        return self.properties["n_connections"]

    def get_n_simulations(self):
        assert isinstance(self.properties["n_simulations"], int)
        return self.properties["n_simulations"]

    def get_slot_size(self):
        assert not isinstance(self.properties["slot_size"], str)
        return self.properties["slot_size"]

    def get_n_cores(self):
        assert isinstance(self.properties["n_cores"], int)
        return self.properties["n_cores"]

    def get_cores(self):
        return np.arange(self.get_n_cores())

    def get_core_selection_fn(self):
        return CORE_SELECTION_FN[self.get_type_core_selection()]

    def get_file_topology(self):
        assert self.topologies.__contains__(self.properties["file_topology"]), "Invalid topology."
        return self.properties["file_topology"]

    def get_bandwidth(self):
        assert isinstance(self.properties["bandwidth"], int)
        return self.properties["bandwidth"]

    def get_traffic_lambda(self):
        return np.array(self.properties["traffic_lambda"])

    def get_traffic_refresh(self):
        assert isinstance(self.properties["traffic_refresh"], bool)
        return self.properties["traffic_refresh"]

    def get_traffic_file(self):
        assert isinstance(self.properties["traffic_file"], bool)
        return self.properties["traffic_file"]

    def get_traffic_conn_types(self):
        return np.array(self.properties["traffic_conn_types"])

    def get_traffic_repeat_times(self):
        return np.array(self.properties["traffic_repeat_times"])

    def get_traffic_conn_probs(self):
        return np.array(self.properties["traffic_conn_probs"])

    def get_route_algorithm(self):
        assert isinstance(self.properties["route_algorithm"], str)
        return self.properties["route_algorithm"]

    def get_k_routes(self):
        assert isinstance(self.properties["k_routes"], int)
        return self.properties["k_routes"]

    def get_route_selection(self):
        assert isinstance(self.properties["route_selection"], str)
        return self.properties["route_selection"]

    def get_pcc_holding_time(self):
        assert isinstance(self.properties["pcc_holding_time"], int)
        return self.properties["pcc_holding_time"]

    def get_guard_band(self):
        assert type(self.properties["guard_band"]) is int, "`guard_band` type must be int"
        return self.properties["guard_band"]

    def get_fiber_allocation(self):
        return self.properties["fiber_allocation"]

    def get_conn_holding_time(self):
        return self.properties["connection_holding_time"]

    def get_tracer(self):
        return self.properties["tracer"]

    def get_osnr(self):
        return self.properties["osnr"]

    def get_modulation(self):
        return self.properties["modulation"]

    def get_lambda(self):
        return self.properties["lambda"]

    def get_fn(self):
        return self.properties["fn"]

    def get_p(self):
        return self.properties["p"]

    def get_span_length(self):
        return self.properties["span_length"]

    def get_node_loss(self):
        return self.properties["node_loss"]

    def get_band_ref(self):
        return self.properties["bandwidth_reference"]

    def get_limit_single_carrier(self):
        assert isinstance(self.properties["limit_single_carrier"], int)
        return self.properties["limit_single_carrier"]

    def get_wavelength(self):
        return self.properties["wavelength"]

    def get_bending_radius(self):
        return self.properties["bending_radius"]

    def get_coupling_coeff(self):
        return self.properties["coupling_coeff"]

    def get_core_pitch(self):
        return self.properties["core_pitch"]

    def get_port_isolation(self):
        return self.properties["port_isolation"]

    def get_crosstalk_tracer(self):
        return self.properties["crosstalk_tracer"]

    def get_crosstalk_reason(self):
        return self.properties["crosstalk_reason"]

    def get_calculate_crosstalk(self):
        return self.properties["calculate_crosstalk"]

    def get_type_core_selection(self):
        return self.properties["type_core_selection"]

    def get_greedy(self):
        return self.properties["greedy"]

    def get_save_log_memory(self):
        return self.properties["save_log_memory"]

    def get_confidence_interval(self):
        return self.properties["ci"]

    def get_network_usage(self):
        return self.properties["network_usage"]

    def get_thread_number(self):
        return self.properties["thread_number"]

    def get_bulk_provision(self):
        return self.properties["bulk_provision"]

    def get_pcc_time_threshold(self):
        return self.properties["pcc_time_threshold"]

    def get_bundles_threshold(self):
        return self.properties["bundles_threshold"]

    def get_min(self):
        return self.properties["min"]

    def get_max(self):
        return self.properties["max"]

    def get_command_log(self):
        return self.properties["command_log"]

    def get_ber_type(self):
        assert self.properties[
                   "osnr_ber_type"] in self.fm.dict_osnr.keys(), f"BER must Be in {self.fm.dict_osnr.keys()}"
        return self.properties["osnr_ber_type"]

    def get_time_avg_log(self):
        return self.properties["time_avg_log"]

