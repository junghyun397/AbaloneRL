import args_parser
from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic

args = args_parser.get_parser().parse_args()

if __name__ == '__main__':
    env = AbaloneEnvironment()

    graphic = TextGraphic() if args.graphic == "text" else Qt5Graphic()
    graphic.init_ui(env.abalone_model.game_vector)
