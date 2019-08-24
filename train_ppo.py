from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic

graphic_mode = "TEXT"

if __name__ == '__main__':
    env = AbaloneEnvironment()

    graphic = Qt5Graphic(env.abalone_model.game_vector) if graphic_mode.lower() == "qt5"\
        else TextGraphic(env.abalone_model.game_vector)
