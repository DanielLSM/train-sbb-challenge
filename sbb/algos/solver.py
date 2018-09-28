import logging
import sbb.tools.logger

from sbb.tools.api import Instances

from abc import ABC, abstractmethod

logger = logging.getLogger('APILogger')


class BaseSolver(ABC):

    def __init__(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def solve(self):
        pass


class MixedIntegerSolver(BaseSolver):

    def __init__(self, *args, **kwargs):
        super().__init__()
        pass


if __name__ == '__main__':
    # instance = Iapi()
    # print(instance)
    # paths = instance.generate_all_paths(111)
    # a = paths[0][0]
    # b = paths[0][-1]
    # paths = instance.generate_paths(111, a, b)
    # paths1 = instance.generate_edge_paths(111, a, b)
