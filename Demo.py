import random

from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic


def random_policy(action_space: int) -> list:
    return [random.randrange(0, action_space),
            random.randrange(0, action_space),
            random.randrange(0, action_space)]


graphic_mode = "TEXT"

if __name__ == '__main__':
    env = AbaloneEnvironment()
    if graphic_mode.lower() == "qt5":
        graphic = Qt5Graphic(base_vector=env.abalone_model.game_vector)
    else:
        graphic = TextGraphic(base_vector=env.abalone_model.game_vector)

    turns = 0
    while True:
        _, info = env.action(random_policy(env.action_space))
        _, drops, _, _, end = info
        turns += 1
        if end:
            graphic.update_vector(new_vector=env.abalone_model.game_vector)
            graphic.draw()
