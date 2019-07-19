from abc import ABCMeta

from abalone.AbaloneModel import AbaloneAgent


class TreeSearchAgent(metaclass=ABCMeta):

    def __init__(self, agent: AbaloneAgent):
        self.agent = agent
