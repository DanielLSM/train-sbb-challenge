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

    def section_variables(self) -> dict:
        return NotImplemented

    def temporal_variables(self) -> dict:
        return NotImplemented

    @abstractmethod
    def define_variables(self) -> dict:
        return NotImplemented

    @property
    @abstractmethod
    def cardinality(self) -> int:
        return NotImplemented


class MixedIntegerFormulator(ProblemStament):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.instance = Instances(ninstance, input_dir)
        self.logger.info('MILP initiated')

    def define_variables(self) -> dict:
        return NotImplemented

    @property
    def cardinality(self) -> int:
        return NotImplemented


if __name__ == '__main__':

    milp = MixedIntegerFormulator()
    # instance = Instances()
    # print(instance)
    # paths = instance.generate_all_paths(111)
    # a = paths[0][0]
    # b = paths[0][-1]
    # paths = instance.generate_paths(111, a, b)
    # paths1 = instance.generate_edge_paths(111, a, b)
