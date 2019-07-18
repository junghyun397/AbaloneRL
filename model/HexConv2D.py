import tensorflow as tf

from abalone import AbaloneModel


class HexConv2D(tf.keras.layers):

    def __init__(self, num_outputs):
        super(HexConv2D, self).__init__()
        self.num_outputs = num_outputs
        self.edge_size = AbaloneModel.get_edge_size(num_outputs)
        self.get_1d_pos = AbaloneModel.get_pos_method(edge_size=self.edge_size)

    def build(self, input_shape):
        self.kernels = None

    def call(self, inputs):
        pass
