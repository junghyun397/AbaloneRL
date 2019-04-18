from abalone.AbaloneModel import AbaloneModel
from abalone.FieldTemplate import FieldTemplate


class AbaloneAgent:

    def __init__(self, abalone_model: AbaloneModel = AbaloneModel(field=FieldTemplate.EDGE_5_BELGIAN_DAISY)):
        self._abalone_model = abalone_model

    def setup_game(self):
        pass
