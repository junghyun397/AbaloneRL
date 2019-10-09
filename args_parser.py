import argparse

parser = argparse.ArgumentParser(description="AbaloneRL executable")
parser.add_argument("-s", "--board-size", help="set Abalone-game board-size (default: 5)",
                    type=int, default=5)
parser.add_argument("-g", "--graphic", help="set graphic interface type (default: text)",
                    type=str, default="text")
parser.add_argument("-a", "--algorithm", help="set Algorithm type (default: alphazero)",
                    type=str, default="alphazero")


def add_train_option():
    parser.add_argument("-b", "--batch-size", help="set training batch(replay)-size (default: 20)",
                        type=int, default=20)
    parser.add_argument("-l", "--learning-rate", help="set learning-rate (default: Adam Optimizer; 0.001)",
                        type=float, default=0.001)
