import tensorflow as tf
import tensorflow.contrib as tf_contrib

from abalone import AbaloneModel


def hex_conv_2d(edge_size: int):
    get_1d_pos, _ = AbaloneModel.build_indexed_pos_method(edge_size)

    def hex_conv_2d_layer(x, kernel=4, use_bias=True, scope="hex_conv_2d"):
        with tf.variable_scope(scope):
            pass
        return x

    return hex_conv_2d_layer


def hex_max_pooling_2d():

    def hex_max_pooling_2d_layer(x, kernel=4, use_bias=True, scope="hex_conv_2d"):
        with tf.variable_scope(scope):
            pass
        return x

    return hex_max_pooling_2d_layer


def hex_avg_pooling_2d():

    def hex_avg_pooling_2d_layer(x, use_bias=True, scope="hex_avg_pooling_2d"):
        with tf.variable_scope(scope):
            pass
        return x

    return hex_avg_pooling_2d_layer
