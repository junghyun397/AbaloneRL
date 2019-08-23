from abalone import AbaloneModel
from agent.PruningPolicy import PruningPolicy


class Node:

    def expand(self):
        pass

    def select(self):
        pass

    def update(self):
        pass

    def update_all(self):
        pass


class AbaloneMCTS:

    def __init__(self,
                 abalone_agent: AbaloneModel.AbaloneAgent,
                 pruning_policy: PruningPolicy):
        super().__init__()
        self.agent = abalone_agent
        self.pruning_policy = pruning_policy

    def next(self):
        pass

    def get_action_scores(self):
        pass
