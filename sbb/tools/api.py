import logging
import sbb.tools.logger
from sbb.tools.parsers import parse_input_paths, parse_json_file
from sbb.tools import input_dir


class InstanceAPI:

    def __init__(self, ninstance: int = 0, input_dir: str = input_dir):
        self._ninstance = ninstance
        self._input_dir = input_dir
        self._ipaths = parse_input_paths(input_dir)
        self.data = self._load_data(ninstance)
        self.api_logger = logging.getLogger('APIlogger')
        self.api_logger.setLevel(logging.INFO)
        self.api_logger.info('API for the Instances Initialized')

    def _load_data(self, ni: int) -> dict:
        try:
            return parse_json_file(self._ipaths[ni])
        except ValueError as e:
            self.api_logger.ERROR(
                "Select an instance from 1 to {}".format(len(self._ipaths) + 1))
            raise e
