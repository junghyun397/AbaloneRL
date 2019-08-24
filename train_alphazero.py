from abalone.AbaloneModel import AbaloneAgent
from agent.RandomPruningPolicy import RandomPruningPolicy
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic
from model.AbaloneMCTS import AbaloneMCTS


graphic_mode = "TEXT"

if __name__ == '__main__':
    abalone_model = AbaloneAgent()

    pruning_policy = RandomPruningPolicy()
    mcts = AbaloneMCTS(abalone_model, pruning_policy)

    graphic = Qt5Graphic(abalone_model.game_vector) if graphic_mode.lower() == "qt5"\
        else TextGraphic(abalone_model.game_vector)
