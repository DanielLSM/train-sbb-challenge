import logging
import sbb.tools.logger

from sbb.tools.api import InstanceAPI as Iapi

logger = logging.getLogger('APILogger')

if __name__ == '__main__':
    instance = Iapi()
    print(instance)
    paths = instance.generate_all_paths(111)

