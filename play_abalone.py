import args_parser
from abalone import FieldTemplate
from abalone.AbaloneModel import AbaloneAgent
from graphics.QSyncManager import iteration_queue, SyncType
from graphics.qt5.Qt5PlayableGraphic import Qt5PlayableGraphic
from model.AbalonePlayController import AbalonePlayController

args = args_parser.get_parser(add_graphic_option=False).parse_args()

if __name__ == '__main__':
    abalone_model = AbaloneAgent(edge_size=args.board_size,
                                 vector_generator=FieldTemplate.basic_start)

    graphic_agent = Qt5PlayableGraphic()

    abalone_play_controller = AbalonePlayController(abalone_model=abalone_model, sync_queue=graphic_agent.sync_queue)

    graphic_agent.init_ui(abalone_model.game_vector)

    while True:
        for event in iteration_queue(graphic_agent.handler_queue):
            if event.sync_type == SyncType.SYNC_CLICK:
                abalone_play_controller.click_stone_event(event.y, event.x)
            elif event.sync_type == SyncType.SYNC_ENTER:
                abalone_play_controller.enter_event()
