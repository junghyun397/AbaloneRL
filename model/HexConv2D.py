import numpy as np
import tensorflow as tf

from abalone import AbaloneModel


class HexConv2D(tf.keras.layers):

    def __init__(self, num_outputs, kernel_size: int = 3):
        super(HexConv2D, self).__init__()
        self.num_outputs = num_outputs
        self.kernel_size = AbaloneModel.get_field_size(kernel_size)
        self.get_1d_pos, self.get_2d_pos = None, None

    # noinspection PyAttributeOutsideInit
    def build(self, input_shape):
        self.edge_size = AbaloneModel.get_edge_size(field_size=input_shape)
        self.get_1d_pos, self.get_2d_pos = AbaloneModel.get_pos_method(edge_size=self.edge_size)
        self.kernels = np.array([[0] for _ in range(29)], dtype=np.uint16)

    def call(self, inputs):
        return inputs * self.kernels
