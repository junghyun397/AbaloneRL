# TODO: implement train-alphazero

import args_parser
from abalone.AbaloneModel import AbaloneAgent
from agent.pruning.RandomPruningPolicy import RandomPruningPolicy
from graphics.qt5.Qt5Graphic import Qt5Graphic
from graphics.text.TextGraphic import TextGraphic
from model.AbaloneMCTS import AbaloneMCTS


args = args_parser.get_parser().parse_args()

if __name__ == '__main__':
    abalone_model = AbaloneAgent()

    pruning_policy = RandomPruningPolicy()
    mcts = AbaloneMCTS(abalone_model, pruning_policy)

    graphic = TextGraphic() if args.graphic == "text" else Qt5Graphic()
    graphic.init_ui(abalone_model.game_vector)
