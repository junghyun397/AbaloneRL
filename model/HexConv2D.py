import numpy as np
import tensorflow as tf

from abalone import AbaloneModel


def hex_conv_2d(nOutputPlane, kW, kH, dW=1, dH=1, padding="VALID", bias=True, reuse=False,
                name="AbaloneHexConv2D"):
    def hex_conv_2d_layer(x, is_training=True):
        edge_size = AbaloneModel.get_edge_size(x.get_shape()[3])
        n_input_plane = x.get_shape().as_list()[3]
        with tf.variable_scope(name, None, [x], reuse=reuse):
            w = tf.get_variable('weight', [kH, kW, n_input_plane, nOutputPlane],
                            initializer=tf.initializers.tables_initializer)
            b = None

    return hex_conv_2d_layer


def hex_max_pooling_2d():
    def hex_max_pooling_2d_layer(x, is_training=True):
        pass

    return hex_max_pooling_2d_layer


def hex_avg_pooling_2d():
    def hex_avg_pooling_2d_layer(x, is_training=True):
        pass

    return hex_avg_pooling_2d_layer
