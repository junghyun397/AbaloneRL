import random

from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic


def random_policy(action_space: int) -> list:
    return [random.randrange(0, action_space), random.randrange(0, action_space), random.randrange(0, action_space)]


graphic_mode = "TEXT"

if __name__ == '__main__':
    env = AbaloneEnvironment()
    graphic = Qt5Graphic(env.abalone_model.game_vector) if graphic_mode.lower() == "qt5"\
        else TextGraphic(env.abalone_model.game_vector)

    total_game, max_turns = 0, 0
    while True:
        _, info = env.action(random_policy(env.action_space))
        _, drops, _, _, end = info
        if end:
            total_game += 1
            if not total_game % 100:
                graphic.draw()
                print(total_game)
                graphic.set_vector(new_vector=env.abalone_model.game_vector)