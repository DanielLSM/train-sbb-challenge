import logging
import sbb.tools.logger

from abc import ABC, abstractmethod


class Validator(ABC):

    @abstractmethod
    def __init__(self, *args, **kwargs):
        self.logging.getLogger('APIlogger')
        self.logger.setLevel(logging.INFO)
        self.instance = Instances(ninstance, input_dir)

    @abstractmethod
    def validate(self, solution) -> list:
        """ Picks the solution and returns errors """
        assert 
    
    @property
    @abstractmethod
    def rule_name(self):
        raise NotImplementedError()

