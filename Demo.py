import random

from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic

graphic_mode = "TEXT"

if __name__ == '__main__':
    env = AbaloneEnvironment()
    if graphic_mode.lower() == "qt5":
        graphic = Qt5Graphic(base_vector=env.abalone_model.game_vector)
    else:
        graphic = TextGraphic(base_vector=env.abalone_model.game_vector)

    turns = 0
    while True:
        turns += 1
        game_vector, info = env.action([random.randrange(0, env.action_space),
                                        random.randrange(0, env.action_space),
                                        random.randrange(0, env.action_space)])
        _, _, _, _, end = info
        if end:
            graphic.update_vector(new_vector=env.abalone_model.game_vector)
        graphic.draw()
        print(turns)
