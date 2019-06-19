import tensorflow as tf

from abalone import AbaloneModel


class HexConv2D(tf.keras.layers.Conv2D):

    def __init__(self, num_outputs, filters, kernel_size, **kwargs):
        super().__init__(filters, kernel_size, **kwargs)
        self.num_outputs = num_outputs

    # noinspection PyAttributeOutsideInit
    def build(self, input_shape):
        edge_size = AbaloneModel.get_edge_size(input_shape/6)
        self._get_1d_pos, _ = AbaloneModel.get_pos_method(edge_size)

    def call(self, input):
        pass

    def _get_1d_pos(self, y: int, x: int) -> int:
        pass
