import logging
import sbb.tools.logger
import pprint

from sbb.tools.parsers import parse_input_paths, parse_json_file
from sbb.tools import input_dir


class InstanceAPI:

    def __init__(self, ninstance: int = 0, input_dir: str = input_dir):
        self._input_dir = input_dir
        self._ipaths = parse_input_paths(input_dir)

        self.api_logger = logging.getLogger('APIlogger')
        self.api_logger.setLevel(logging.INFO)

        self.data = self.load_data(ninstance)
        self._fname = self.data['label']
        self.api_logger.info('API for the Instances Initialized')

    def __str__(self):
        return 'API to interface instance {}'.format(self._fname)

    def load_data(self, ninstance: int) -> dict:
        try:
            self.api_logger.info('loaded {}'.format(
                self._ipaths[ninstance].parts[-1]))
            return parse_json_file(self._ipaths[ninstance])
        except ValueError as e:
            self.api_logger.ERROR(
                "Select an instance from 1 to {}".format(len(self._ipaths) + 1))
            raise e

    # def inspect(self, key: str):
    #     return pprint.pprint(self.data[key])