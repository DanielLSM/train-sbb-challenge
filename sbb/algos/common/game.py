import logging
import numpy as np
from abc import ABC, abstractmethod
from collections import defaultdict
from gym.spaces.box import Box
from itertools import product, chain, permutations

import sbb.tools.logger
from sbb.tools.instances import Instances
from sbb.tools import input_dir, input_samples


class GameEngine(ABC):

    @abstractmethod
    def __init__(self,
                 ninstance: int = 0,
                 input_dir: str = input_samples,
                 *args,
                 **kwargs):
        self.logger = logging.getLogger('APIlogger')
        self.logger.setLevel(logging.INFO)
        self.instance = Instances(ninstance, input_dir)

    @abstractmethod
    def _generate_discrete_state_space(self) -> dict:
        return NotImplementedError()

    @abstractmethod
    def _generate_vars_iter(self) -> dict:
        return NotImplementedError()

    @abstractmethod
    def _generate_vars(self) -> dict:
        return NotImplementedError()

    @property
    @abstractmethod
    def cardinality(self) -> int:
        return NotImplementedError()


class ScheduleGame(GameEngine):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger.info('A game of scheduling =)')
        self.discrete_state_space = self._generate_discrete_state_space()

        #TODO: actually understand what is the action space XDDDDD
        # self.action_space = Box(low=-10,high=10,shape(1,))

    def sample_discrete_state_space(self):
        sample = defaultdict(list)
        for train_id in self.discrete_state_space.keys():
            # import pdb; pdb.set_trace()
            sample[train_id] = np.random.choice(
                self.discrete_state_space[train_id])
        return sample

    def _generate_discrete_state_space(self) -> dict:
        """ Generates a macro level state space, e.g, combinations of 
        sections for each train """
        discrete_state_space = defaultdict(list)
        for train in self.instance['service_intentions']:
            discrete_state_space[train['id']] = self._generate_vars(train['id'])
        return discrete_state_space

    def _generate_vars(self, train_id) -> list:
        """ given a train_id a generator is given, yielding vars 
        here we generate temporal and sections vars
        """
        markers = [
            marker_rec['section_marker'] for marker_rec in self.instance
            .service_intentions[train_id]['section_requirements']
        ]

        route_id = self.instance.service_intentions[train_id]['route']
        req_marker_sections = [
            self.instance.route2marker2sections[route_id][marker]
            for marker in markers
        ]

        all_paths = []
        for requirements in product(*req_marker_sections):
            for path in self.instance.paths_from_arcs(route_id, requirements):
                all_paths.append(['{}#{}'.format(route_id, k) for k in path])
        return all_paths

    def _generate_vars_iter(self, train_id) -> iter:
        # TODO: Dont want a generator, I want all possibilites available
        """ given a train_id a generator is given, yielding vars 
        here we generate temporal and sections vars
        """
        markers = [
            marker_rec['section_marker'] for marker_rec in self.instance
            .service_intentions[train_id]['section_requirements']
        ]

        route_id = self.instance.service_intentions[train_id]['route']
        req_marker_sections = [
            self.instance.route2marker2sections[route_id][marker]
            for marker in markers
        ]

        # TODO: * means passing as argumentssssss xd
        # TODO: more than one train retard
        import pdb
        pdb.set_trace()
        for requirements in product(*req_marker_sections):
            for path in self.instance.paths_from_arcs(route_id, requirements):
                yield ['{}#{}'.format(route_id, k) for k in path]

        #TODO give me paths based on edges for simplicity please, done
        # for requirements in permu
        # yield self.instance.paths_from_arcs(route_id, [1, 5, 14])

    @property
    def cardinality(self) -> int:
        return NotImplemented


if __name__ == '__main__':

    sp = ScheduleGame()
    sample = sp.sample_discrete_state_space()
