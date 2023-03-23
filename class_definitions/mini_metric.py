import tensorflow as tf
import keras


class Tracker(keras.metrics.Metric):

    """Docstring for MyClass. """

    def __init__(self, name, **kwargs):
        """TODO: to be defined. """
        super().__init__(name=name, **kwargs)

    def update_state(self, fwise_loss):
        """TODO: Docstring for update_state.

        :fwise_loss: TODO
        :returns: TODO

        """
        if not hasattr(self, "fwise_losses"):
            self.fwise_losses = tf.cast(fwise_loss, dtype=tf.float32)
        else:
            tf.concat([self.fwlosses, fwise_loss], axis=1)


    def result(self):
        """TODO: Docstring for result.
        :returns: TODO

        """
        return self.fwise_losses
