from abalone import AbaloneModel
from agent.NeuralNetwork import NeuralNetwork
from agent.TreeSearchAgent import TreeSearchAgent


class AbaloneMCTS(metaclass=TreeSearchAgent):

    def __init__(self,
                 abalone_agent: AbaloneModel.AbaloneAgent,
                 policy_network: NeuralNetwork):
        self.agent = abalone_agent
        self.t_agent = abalone_agent.copy()
        self.policy_network = policy_network

    def precess_next(self) -> dict:
        merge_vec = dict()
        for action in range(self.agent.field_size):

            t_moved = 0
            while t_moved < 3:
                decoded_action = self.agent.decode_action(action)
                line, moved, dropped = self.agent.can_push_stone(*decoded_action)

                if line is not None:
                    t_moved += moved

                    self.t_agent.set_game_vector(self.agent.game_vector.copy())
                    self.t_agent.push_stone(*decoded_action)
                    merge_vec[action] = self.t_agent.game_vector, moved, dropped
        return merge_vec
