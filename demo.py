import random
from typing import Callable

from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.TextGraphic import TextGraphic


def build_random_policy(action_space: int) -> Callable[[], int]:
    def random_policy():
        return random.randrange(0, action_space)

    return random_policy


if __name__ == '__main__':
    env = AbaloneEnvironment()
    graphic = TextGraphic(env.abalone_model.game_vector)
    graphic.set_vector(env.abalone_model.game_vector)

    policy = build_random_policy(env.abalone_model.field_size * 6)

    while True:
        _, info = env.action([policy(), policy(), policy()])
        _, _, _, _, end = info

        if end:
            graphic.draw()
            graphic.set_vector(env.abalone_model.game_vector)
