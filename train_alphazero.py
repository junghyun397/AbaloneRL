import args_parser
from abalone.AbaloneModel import AbaloneAgent
from agent.RandomPruningPolicy import RandomPruningPolicy
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic
from model.AbaloneMCTS import AbaloneMCTS


args = args_parser.get_parser().parse_args()

if __name__ == '__main__':
    abalone_model = AbaloneAgent()

    pruning_policy = RandomPruningPolicy()
    mcts = AbaloneMCTS(abalone_model, pruning_policy)

    graphic = TextGraphic() if args.graphic == "text" else Qt5Graphic()
    graphic.init_ui(abalone_model.game_vector)
