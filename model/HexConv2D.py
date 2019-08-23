import tensorflow as tf
import tensorflow.contrib as tf_contrib

from abalone import AbaloneModel


def hex_conv_2d(x, kernel=4, use_bias=True, scope="hex_conv_2d"):
    edge_size = x.shape[3]
    with tf.variable_scope(scope):
        pass
    return x


def hex_max_pooling_2d(x, use_bias=True, scope="hex_max_pooling_2d"):
    with tf.variable_scope(scope):
        pass
    return x


def hex_avg_pooling_2d(x, use_bias=True, scope="hex_avg_pooling_2d"):
    with tf.variable_scope(scope):
        pass
    return x
