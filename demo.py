import random

import args_parser
from abalone import FieldTemplate
from abalone.AbaloneModel import AbaloneAgent
from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic


def random_policy(action_space: int) -> list:
    return [random.randrange(0, action_space), random.randrange(0, action_space), random.randrange(0, action_space)]


args = args_parser.parser.parse_args()

if __name__ == '__main__':
    abalone_model = AbaloneAgent(edge_size=args.board_size,
                                 vector_generator=FieldTemplate.basic_start)
    env = AbaloneEnvironment(abalone_model)

    graphic = TextGraphic() if args.graphic == "text" else Qt5Graphic()
    graphic.init_ui(env.abalone_model.game_vector)

    game_success, game_total = 0, 0
    total_game, max_turns = 0, 0
    while True:
        _, info = env.action(random_policy(env.action_space))
        success, drops, _, _, end = info
        game_success += sum(success)
        game_total += 3
        if end:
            total_game += 1
            if not total_game % 100:
                graphic.draw()
                print("++total-game: {0}, local-success: {1}, local-turns: {2}"
                      .format(total_game, game_success, game_total))
                graphic.update_game_vector(env.abalone_model.game_vector)
            game_success, game_total = 0, 0
