from abalone.AbaloneModel import AbaloneAgent
from graphics.TextGraphic import TextGraphic
from model.AbaloneMCTS import AbaloneMCTS
from model.HexNetPruningModel import HexNetPruningModel
from model.HexProbNetwork import HexProbNetwork


if __name__ == '__main__':
    agent = AbaloneAgent()
    hex_conv_n_network = HexProbNetwork()
    pruning_network = HexNetPruningModel(hex_prob_network=hex_conv_n_network)
    mcts = AbaloneMCTS(abalone_agent=agent, pruning_policy=pruning_network)

    graphic = TextGraphic()
    graphic.set_vector(agent.game_vector)
