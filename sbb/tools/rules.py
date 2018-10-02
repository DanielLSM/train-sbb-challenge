import logging
import sbb.tools.logger

from abc import ABC, abstractmethod

from sbb.tools.instances import Instances
from sbb.tools import input_dir, input_samples


class Validator(ABC):

    @abstractmethod
    def __init__(self,
                 ninstance: int = 0,
                 input_dir: str = input_samples,
                 *args,
                 **kwargs):
        self.logging.getLogger('APIlogger')
        self.logger.setLevel(logging.INFO)
        self.instance = Instances(ninstance, input_dir)

    @abstractmethod
    def validate(self, solution) -> list:
        """ Picks the solution and returns errors """
        raise NotImplementedError()

    @property
    @abstractmethod
    def rules_names(self):
        raise NotImplementedError()


class ConsistencyRules(Validator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger.info('Constency Rules instanciated')
        self._rules = {
            '#1': {
                'name': 'problem_instance_hash present',
                'rule_defination': self._problem_instance_hash_present
            },
            '#2': {
                'name': 'each train is scheduled',
                'rule_defination': self._each_trained_is_scheduled
            },
            '#3': {
                'name': 'ordered train_run_sections',
                'rule_defination': self._ordered_trains
            },
            '#4': {
                'name':
                    'Reference a valid route, route_path and route_section',
                'rule_defination':
                    self._valid_route_path_section
            },
            '#5': {
                'name': 'train_run_sections form a path in the route graph',
                'rule_defination': self._sections_form_path
            },
            '#6': {
                'name': 'pass through all section_requirements',
                'rule_defination': self._check_all_section_requirements
            },
            '#7': {
                'name': 'consistent entry_time and exit_time times',
                'rule_defination': self._consistent_entry_exit
            }
        }

    def validate(self, solution):
        errors = []
        for key in self._rules.keys():
            raise NotImplementedError()

    @property
    def rules_names(self):
        for key in self._rules.keys():
            print('Rule {}: {}\n'.format(key, self._rules[key]['name']))

    #1
    def _problem_instance_hash_present(self):
        raise NotImplementedError()

    #2
    def _each_trained_is_scheduled(self):
        raise NotImplementedError()

    #3
    def _ordered_trains(self):
        raise NotImplementedError()

    #4
    def _valid_route_path_section(self):
        raise NotImplementedError()

    #5
    def _sections_form_path(self):
        raise NotImplementedError()

    #6
    def _check_all_section_requirements(self):
        raise NotImplementedError()

    #7
    def _consistent_entry_exit(self):
        raise NotImplementedError()
