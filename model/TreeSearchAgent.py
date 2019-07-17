import numpy as np

from abalone.AbaloneModel import AbaloneAgent


class TreeSearchAgent:

    def __init__(self, agent: AbaloneAgent):
        self.agent = agent

    def next_step(self, role_vector: np.ndarray, game_vector: np.ndarray) -> np.ndarray:
        pass

    def find_able_move(self, game_vector: np.ndarray) -> np.ndarray:
        pass
