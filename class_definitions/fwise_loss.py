"""
File: fwise_loss.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: Knock-off loss from keras.metrics.mean_squared_error to compute
feature wise mse
"""
from keras import backend
import tensorflow as tf


def mean_squared_error(y_true, y_pred):
    """
    `loss = mean(square(y_true - y_pred), axis=0)`
    Args:
      y_true: Ground truth values. shape = `[batch_size, d0, .. dN]`.
      y_pred: The predicted values. shape = `[batch_size, d0, .. dN]`.
    Returns:
      Mean squared error values. shape = `[batch_size, d0, .. dN-1]`.
    """
    y_pred = tf.convert_to_tensor(y_pred)
    y_true = tf.cast(y_true, y_pred.dtype)
    return backend.mean(tf.math.squared_difference(y_pred, y_true), axis=0)
