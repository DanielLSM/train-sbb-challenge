import logging
import sbb.tools.logger

from abc import ABC, abstractmethod

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
        # self.trains =

    def generate_section_vars(self, train_id: int, route_id: int, start: str,
                              finish: str) -> dict:
        # try:
        #     self.instance.data['service_intentions']

        return NotImplemented

    def generate_temporal_vars(self) -> dict:
        return NotImplemented

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

    def generate_vars(self) -> dict:
        return NotImplemented

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
    nodes = ['(1_beginning)', '(M2)', '(14_end)']
    route_id = 111
    milp.instance.generate_paths_from_nodes(route_id, nodes)

    # instance = Instances()
    # print(instance)
    # paths = instance.generate_all_paths(111)
    # a = paths[0][0]
    # b = paths[0][-1]
    # paths = instance.generate_paths(111, a, b)
    # paths1 = instance.generate_edge_paths(111, a, b)
