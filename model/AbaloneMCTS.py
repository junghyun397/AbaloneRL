import numpy as np

from abalone import AbaloneModel
from agent.NeuralNetwork import NeuralNetwork
from agent.PruningPolicy import PruningPolicy


class AbaloneMCTS(PruningPolicy):

    def __init__(self,
                 abalone_agent: AbaloneModel.AbaloneAgent,
                 policy_network: NeuralNetwork):
        super().__init__()
        self.agent = abalone_agent
        self.t_agent = abalone_agent.copy()
        self.policy_network = policy_network

    def prediction(self, source_vector: np.ndarray) -> float:
        pass

    def find_next_move(self, state_vector) -> dict:
        self.t_agent.set_game_vector(state_vector)
        merged_vec = dict()
        for act in range(self.agent.field_size):
            lin, _, _ = self.agent.can_push_stone(*self.t_agent.decode_action(act))
            if lin is not None:
                merged_vec[act] = 0
        return merged_vec
