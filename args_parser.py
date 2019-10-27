import argparse

_parser = argparse.ArgumentParser(description="AbaloneRL executable")

_parser.add_argument("-s", "--board-size", dest="board_size",
                     help="set Abalone-game board-size (default: 5)",
                     type=int, default=5)


def _add_graphic_option():
    _parser.add_argument("-g", "--graphic", dest="graphic",
                         help="set graphic interface type (default: text)",
                         type=str, default="text")


def _add_train_option():
    _parser.add_argument("-b", "--batch-size", dest="batch_size",
                         help="set training batch(replay)-size (default: 20)",
                         type=int, default=20)
    _parser.add_argument("-l", "--learning-rate", dest="learning_rate",
                         help="set learning-rate (default: Adam Optimizer; 0.001)",
                         type=float, default=0.001)
    _parser.add_argument("-r", "--replay-size", dest="replay_size",
                         help="set replay-memory-size (default: 10000)",
                         type=int, default=10000)


def get_parser(add_graphic_option=True,
               add_train_option=False):
    if add_graphic_option:
        _add_graphic_option()
    if add_train_option:
        _add_train_option()

    return _parser
