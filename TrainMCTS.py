from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from model.AbaloneMCTS import AbaloneMCTS
from model.HexProbNetwork import HexProbNetwork


if __name__ == '__main__':
    env = AbaloneEnvironment()
    policy_network = HexProbNetwork()
    mcts = AbaloneMCTS(env.abalone_model, policy_network)
