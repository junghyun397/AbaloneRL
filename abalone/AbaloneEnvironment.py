import numpy as np

from abalone.AbaloneModel import AbaloneModel
from abalone.FieldTemplate import FieldTemplate


class AbaloneEnvironment:

    def __init__(self, abalone_model: AbaloneModel = AbaloneModel(edge_size=5, field=FieldTemplate.EDGE_5_BELGIAN_DAISY)):
        self.abalone_model = abalone_model

    def action(self, action: int):
        return self.get_vector_state()

    def get_vector_state(self) -> np.ndarray:
        return self.abalone_model.copy_field()
