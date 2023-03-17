import networkx as nx
from itertools import islice


class Router:
    def __init__(self, params):
        self.graph = params.get_topology()[0]
        self._edges = {(source, target): weight["weight"] for (source, target, weight) in self.graph.edges(data=True)}
        self.learned_paths = {}

    @staticmethod
    def _format_name(source, target, k):
        return f"s{source}t{target}k{k}"

    @staticmethod
    def _convert(routes):
        return [[(paths[i], paths[i+1]) for i in range(len(paths)-1)] for paths in routes]

    def shortest_paths(self, source, target, weight='weight', k=3):
        path_name = self._format_name(source, target, k)

        if self.learned_paths.__contains__(path_name):
            return self.learned_paths[path_name]

        shortest_paths = nx.shortest_simple_paths(self.graph, source, target, weight)
        self.learned_paths[path_name] = self._convert(list(islice(shortest_paths, k)))
        return self.learned_paths[path_name]

    def calc_total_weight(self, routes):
        return sum(map(self.calc_weight, routes))

    def calc_weight(self, route):
        weight_sum = sum([self._edges.get(path) for path in route])
        # for i in range(len(route) - 1):
        #     weight_sum += self._edges[(route[i], route[i + 1])]

        return weight_sum

# r = Router(Parameters())
# print(r.graph.graph)
# print(r.graph.edges())
# print(r.graph.nodes())

# print(r.shortest_paths(0, 1))
