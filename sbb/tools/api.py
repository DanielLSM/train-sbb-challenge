import logging
import sbb.tools.logger
import pprint
import networkx

from itertools import product, starmap
from itertools import chain.from_iterable as chaini
from functools import partial

from sbb.tools.parsers import parse_input_paths, parse_json_file
from sbb.tools import input_dir, input_samples
from sbb.tools.route_graph import generate_route_graphs


class InstanceAPI:

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

    def generate_all_paths(self, route_id: int, start: str, end: str) -> list:
        all_paths = partial(networkx.algorithms.simple_paths.all_simple_paths,
                            self.route_graphs[route_id])
        return list(chaini(starmap(all_paths,start,end)))
        
        # return networkx.algorithms.simple_paths.all_simple_paths(
        #     self.route_graphs[route_id], source=start, target=end)

    def nodes(self, route_id) -> list:
        return self.route_graphs[route_id].nodes()

    def edges(self, route_id) -> list:
        return self.route_graphs[route_id].edges()

    # def inspect(self, key: str):
    #     return pprint.pprint(self.data[key])


if __name__ == '__main__':
    i = InstanceAPI()