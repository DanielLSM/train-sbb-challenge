import logging
import sbb.tools.logger

from abc import ABC, abstractmethod
from itertools import product, chain, permutations

from sbb.tools.instances import Instances
from sbb.tools import input_dir, input_samples


class ProblemStament(ABC):

    @abstractmethod
    def __init__(self,
                 ninstance: int = 0,
                 input_dir: str = input_samples,
                 *args,
                 **kwargs):
        self.logger = logging.getLogger('APIlogger')
        self.logger.setLevel(logging.INFO)
        self.instance = Instances(ninstance, input_dir)

    @abstractmethod
    def generate_vars(self) -> dict:
        return NotImplemented

    @property
    @abstractmethod
    def cardinality(self) -> int:
        return NotImplemented


class MixedIntegerFormulator(ProblemStament):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger.info('MILP initiated')

    def generate_vars(self, train_id) -> iter:
        """ given a train_id a generator is given, yielding vars 
        here we generate temporal and sections vars
        """
        markers = [
            marker_rec['section_marker'] for marker_rec in self.instance
            .service_intentions[train_id]['section_requirements']
        ]

        route = self.instance.service_intentions[train_id]['route']
        req_marker_sections = [
            self.instance.route2marker2sections[route][marker]
            for marker in markers
        ]

        # TODO: * means passing as argumentssssss xd
        # TODO: more than one train retard
        for requirements in product(*req_marker_sections):
            for path in self.instance.paths_from_arcs(route_id, requirements):
                yield ['{}#{}'.format(route_id, k) for k in path]

        #TODO give me paths based on edges for simplicity please, done
        # for requirements in permu
        # yield self.instance.paths_from_arcs(route_id, [1, 5, 14])

    @property
    def cardinality(self) -> int:
        return NotImplemented


if __name__ == '__main__':

    milp = MixedIntegerFormulator()
    milp.instance.keys()
    train_id = milp.instance.data['service_intentions'][0]['id']
    route_id = milp.instance.data['service_intentions'][0]['route']
    section_requirements = milp.instance.data['service_intentions'][0][
        'section_requirements']
    # milp.instance.route2marker2sections
    # nodes = ['(3_beginning)', '(M2)', '(M3)', '(M4)', '(14_end)']
    nodes = milp.instance.transform_arcs2nodes(111, [1, 5, 14])
    route_id = 111
    milp.instance.paths_from_arcs(route_id, [1, 5, 14])
    # instance = Instances()
    for ppp in milp.generate_vars(111):
        print(ppp)
    # print(instance)
    # paths = instance.generate_all_paths(111)
    # a = paths[0][0]
    # b = paths[0][-1]
    # paths = instance.generate_paths(111, a, b)
    # paths1 = instance.generate_edge_paths(111, a, b)
