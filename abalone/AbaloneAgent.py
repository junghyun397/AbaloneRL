import numpy as np

from abalone.AbaloneModel import AbaloneModel
from abalone.SetupTemplate import SetupTemplate


class AbaloneAgent:

    def __init__(self, abalone_model: AbaloneModel = AbaloneModel(field=SetupTemplate.EDGE_5_BELGIAN_DAISY)):
        self._abalone_model = abalone_model

    def setup_game(self):
        pass
