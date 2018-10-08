import logging
import sbb.tools.logger

from sbb.tools.instances import Instances

logger = logging.getLogger('APILogger')

if __name__ == '__main__':
    instance = InstanceAPI()
    print(instance)
    paths = instance.generate_all_paths(111)
    a = paths[0][0]
    b = paths[0][-1]
    paths = instance.generate_paths(111, a, b)
    paths1 = instance.generate_edge_paths(111, a, b)
