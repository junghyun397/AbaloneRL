from typing import Optional, Tuple

from abalone.HexDescription import HexDescription
from abalone.env.AbaloneEnvironment import AbaloneEnvironment
from graphics.Qt5Graphic import Qt5Graphic
from graphics.TextGraphic import TextGraphic


def parse_text_action(text: str) -> Optional[Tuple[int, int, HexDescription]]:
    spt = text.split(" ")
    return int(spt[0]), int(spt[1]), HexDescription(int(spt[2]))


if __name__ == '__main__':
    graphic = TextGraphic()
    env = AbaloneEnvironment()
    graphic.set_vector(env.abalone_model.game_vector)

    def get_text_base_action() -> list:
        rs_action = [0, 0, 0]
        mut = 0
        while mut < 3:
            print("input move: ")
            pars_rs = parse_text_action(input())
            if pars_rs is not None and (env.abalone_model.can_push_stone(*pars_rs)):
                graphic.draw()
                rs_action[mut] = env.encode_action(*pars_rs)
                mut += 1
            else:
                print("fail move, try again")
        return rs_action

    def get_graphic_base_action() -> list:
        pass

    action_trigger = get_text_base_action

    while True:
        env.action(action=action_trigger())
