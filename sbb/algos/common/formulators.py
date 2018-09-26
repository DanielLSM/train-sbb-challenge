import logging
import sbb.tools.logger

from sbb.tools.api import InstanceAPI as Iapi

logger = logging.getLogger('APILogger')


class ProblemStament:

    def __init__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def passs(self):
        pass


if __name__ == '__main__':
    pass
    # instance = Iapi()
    # print(instance)
    # paths = instance.generate_all_paths(111)
    # a = paths[0][0]
    # b = paths[0][-1]
    # paths = instance.generate_paths(111, a, b)
    # paths1 = instance.generate_edge_paths(111, a, b)
