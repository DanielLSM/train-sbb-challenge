import logging
import sbb.tools.logger
import pprint
import networkx

from itertools import chain, product, starmap
from functools import partial

from sbb.tools.parsers import parse_input_paths, parse_json_file
from sbb.tools import input_dir, input_samples
from sbb.tools.route_graph import generate_route_graphs


class Instances:

    def __init__(self, ninstance: int = 0, input_dir: str = input_samples):
        self._input_dir = input_dir
        self._ipaths = parse_input_paths(input_dir)

        self.api_logger = logging.getLogger('APIlogger')
        self.api_logger.setLevel(logging.INFO)

        self.data = self._load_data(ninstance)
        self.route_graphs = generate_route_graphs(self.data)
        self._fname = self.data['label']
        self.api_logger.info('API for the Instances Initialized')

    def __str__(self):
        return 'API to interface instance {}'.format(self._fname)

    def __getitem__(self, key):
        return pprint.pprint(self.data[key])

    def keys(self):
        return self.data.keys()

    def _load_data(self, ninstance: int) -> dict:
        try:
            self.api_logger.info('loaded {}'.format(
                self._ipaths[ninstance].parts[-1]))
            return parse_json_file(self._ipaths[ninstance])
        except ValueError as e:
            self.api_logger.ERROR("Select an instance from 0 to {}".format(
                len(self._ipaths)))
            raise e

    def nodes(self, route_id) -> list:
        return list(self.route_graphs[route_id].nodes())

    def edges(self, route_id) -> list:
        return list(self.route_graphs[route_id].edges())

    def edges_sn(self, route_id) -> list:
        return self.route_graphs[route_id].edges()

    def generate_paths(self, route_id: int, start: str, end: str) -> list:
        all_paths = partial(networkx.algorithms.simple_paths.all_simple_paths,
                            self.route_graphs[route_id])
        path_iter = all_paths(start, end)
        return list(path_iter)

    def generate_edge_paths(self, route_id: int, start: str, end: str) -> list:
        all_paths = partial(networkx.algorithms.simple_paths.all_simple_paths,
                            self.route_graphs[route_id])
        path_iter = all_paths(start, end)
        paths = []
        edges_info = self.edges_sn(route_id)
        for path in path_iter:
            edges_path = []
            for i in range(len(path) - 1):
                edges_path.append(
                    edges_info[path[i], path[i + 1]]['sequence_number'])
            paths.append(edges_path)
        return paths

    # def generate_paths(self, route_id: int, start: str, end: str) -> list:
    #     all_paths = partial(networkx.algorithms.simple_paths.all_simple_paths,
    #                         self.route_graphs[route_id])
    #     return list(chain.from_iterable(starmap(all_paths, start, end)))

    #TODO generate meaningfull route sections with sequece numbers as needed for the solution
    #TODO get rid of the M1 cancer, we need to generate meaningful variables with times

    def generate_all_paths(self, route_id: int) -> list:
        roots = (
            v for v, d in self.route_graphs[route_id].in_degree() if d == 0)
        leaves = (
            v for v, d in self.route_graphs[route_id].out_degree() if d == 0)
        all_paths = partial(networkx.algorithms.simple_paths.all_simple_paths,
                            self.route_graphs[route_id])
        return list(
            chain.from_iterable(starmap(all_paths, product(roots, leaves))))

    #TODO This is problably the most retarded function of the whole code
    #TODO but I blaim networkx on this one.
    #TODO this func transforms paths written in nodes into paths written in
    #TODO edges
    def from_paths_to_arcs(self, route_id: int, path: list) -> list:
        edges_info = self.edges_sn(route_id)
        edges_path = []
        for i in range(len(path) - 1):
            edges_path.append(
                edges_info[path[i], path[i + 1]]['sequence_number'])
        return edges_path

    # def inspect(self, key: str):
    #     return pprint.pprint(self.data[key])


if __name__ == "__main__":

    i = InstanceAPI()