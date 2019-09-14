import numpy as np
import tensorflow as tf

from abalone import AbaloneModel


def hex_conv_2d(edge_size: int, kernel_edge_size: int, kernel_count: int = 4, scope_name: str = "hex_conv_2d"):
    get_1d_pos, _ = AbaloneModel.build_indexed_pos_method(edge_size)
    hex_kernel = np.zeros((kernel_count, AbaloneModel.get_field_size(kernel_edge_size)), dtype=np.uint8)

    def hex_conv_2d_layer(x, kernel=hex_kernel, scope=scope_name):
        with tf.variable_scope(scope):
            pass
        return x

    return hex_conv_2d_layer


def hex_max_pooling_2d(scope_name: str = "hex_conv_2d"):

    def hex_max_pooling_2d_layer(x, scope=scope_name):
        with tf.variable_scope(scope):
            pass
        return x

    return hex_max_pooling_2d_layer


def hex_avg_pooling_2d(scope_name: str = "hex_avg_pooling_2d"):

    def hex_avg_pooling_2d_layer(x, scope=scope_name):
        with tf.variable_scope(scope):
            pass
        return x

    return hex_avg_pooling_2d_layer
