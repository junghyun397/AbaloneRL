import random

from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic


def random_policy(action_space: int) -> list:
    return [random.randrange(0, action_space), random.randrange(0, action_space), random.randrange(0, action_space)]


graphic_mode = "TEXT"

if __name__ == '__main__':
    if graphic_mode.lower() == "qt5":
        graphic = Qt5Graphic()
    else:
        graphic = TextGraphic()

    trigger = (lambda: graphic.draw())

    env = AbaloneEnvironment()
    graphic.set_vector(env.abalone_model.game_vector)
    total_game = 0
    while True:
        _, info = env.action(random_policy(env.action_space))
        _, drops, _, _, end = info
        total_game += 1
        if end:
            trigger()
            graphic.set_vector(new_vector=env.abalone_model.game_vector)
            print("Total Games: ", total_game)
