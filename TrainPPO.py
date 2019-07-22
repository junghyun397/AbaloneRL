from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.TextGraphic import TextGraphic
from model.HexRNNetwork import HexRNNetwork

if __name__ == '__main__':
    env = AbaloneEnvironment()
    hex_conv_rn_network = HexRNNetwork()

    graphic = TextGraphic()
    graphic.set_vector(env.abalone_model.game_vector)
