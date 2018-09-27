import logging
import sbb.tools.logger

from abc import ABC, abstractmethod

from sbb.tools.instances import Instances

logger = logging.getLogger('APILogger')


class ProblemStament(ABC):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    def section_variables(self):
        return NotImplemented

    def temporal_variables(self):
        return NotImplemented

    @abstractmethod
    def define_variables(self):
        return NotImplemented

    @property
    @abstractmethod
    def cardinality(self):
        return NotImplemented


class MixedIntegerFormulator(ProblemStament):

    def __init__(self):
        pass
        # self.instance = Instances()

    def define_variables(self):
        return NotImplemented

    @property
    def cardinality(self):
        return NotImplemented


if __name__ == '__main__':

    milp = MixedIntegerFormulator()
    instance = Instances()
    # print(instance)
    # paths = instance.generate_all_paths(111)
    # a = paths[0][0]
    # b = paths[0][-1]
    # paths = instance.generate_paths(111, a, b)
    # paths1 = instance.generate_edge_paths(111, a, b)
