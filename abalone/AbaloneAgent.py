import numpy as np

from abalone.AbaloneModel import AbaloneModel


EDGE_5_BASE_START = np.array([0], dtype=np.int8)
EDGE_5_BELGIAN_DAISY = np.array([0], dtype=np.int8)


class AbaloneAgent:

    def __init__(self, abalone_model: AbaloneModel = AbaloneModel(field=EDGE_5_BELGIAN_DAISY)):
        self._abalone_model = abalone_model

    def setup_game(self):
        pass
