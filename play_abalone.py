# TODO: implement play abalone

import args_parser
from abalone import FieldTemplate
from abalone.AbaloneModel import AbaloneAgent
from graphics.QSyncManager import iteration_queue
from graphics.qt5.Qt5PlayableGraphic import Qt5PlayableGraphic

args = args_parser.get_parser(add_graphic_option=False).parse_args()

if __name__ == '__main__':
    abalone_model = AbaloneAgent(edge_size=args.board_size,
                                 vector_generator=FieldTemplate.basic_start)
    graphic_agent = Qt5PlayableGraphic()
    graphic_agent.init_ui(abalone_model.game_vector)

    handler_queue = graphic_agent.handler_queue

    while True:
        for event in iteration_queue(handler_queue):
            pass
