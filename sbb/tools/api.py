import logging
from sbb.tools.parsers import parse_input_paths, parse_json_file
from sbb.tools import input_dir


class InstanceAPI:

    # int: instance_number

    # import pdb
    # pdb.set_trace()

    def __init__(self, ninstance: int = 0, input_dir: str = input_dir):
        self._ninstance = ninstance
        self._input_dir = input_dir
        self.ipaths = parse_input_paths(input_dir)
        self.api_logger = logging.getLogger('APIloger')
        self.api_logger.setLevel(logging.DEBUG)
        self.api_logger.info('API for the Instances Initialized')