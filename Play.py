import random
from typing import Optional, Tuple

from abalone.AbaloneModel import AbaloneAgent
from abalone.HexDescription import HexDescription
from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic


if __name__ == '__main__':
    graphic = TextGraphic()
    agent = AbaloneAgent()
    graphic.set_vector(agent.game_vector)

    while True:
        graphic.draw()
