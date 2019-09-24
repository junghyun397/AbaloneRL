import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--graphic", help="Set graphic interface type", type=str, default="text")
parser.add_argument("-a", "--algorithm", help="Set Algorithm type", type=str, default="alphazero")


def add_train_option():
    parser.add_argument("-b", "--batch_size", help="Set Training batch-size", type=int, default=10)
