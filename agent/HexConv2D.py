import tensorflow as tf


class HexConv2D(tf.keras.layers.Layer):

    def __init__(self, num_outputs):
        super(HexConv2D, self).__init__()
        self.num_outputs = num_outputs

    def build(self, input_shape):
        pass

    # noinspection PyMethodOverriding,PyShadowingBuiltins
    def call(self, input):
        pass
