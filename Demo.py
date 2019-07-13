import random

from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic

if __name__ == '__main__':
    env = AbaloneEnvironment()
    graphic = TextGraphic(base_vector=env.abalone_model.game_vector)
    
    while True:
        vector, reward, end = env.action(random.randrange(0, env.action_space))
        graphic.draw()
