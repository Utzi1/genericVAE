"""
File: gnerator_Class.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: Implments a DataGenerator for gene expression data
"""


from tensorflow import keras
import tensorflow as tf
import numpy as np
import h5py


class DataGenerator(keras.utils.Sequence):
    """
    Will help data-handling of gene expression datafiles from h5 files

    dataset_name: Name of the data (in the h5py structure)
    filepath: path to h5py file
    batch_size: batch_size
    shuffle: defaulted false, however enable with True
    """

    def __init__(self, dataset_name, filepath, batch_size, shuffle=False):
        self.dataset_name = dataset_name
        self.batch_size = batch_size
        self.shuffle = shuffle
        self.filepath = filepath
        # load the data!:
        self.data = h5py.File(filepath, "r").get(dataset_name)
        self._samples_in_set = self.data.shape[0]
        self.on_epoch_end()

    def __len__(self):
        """
        Number of batches each epoche
        """
        return int(np.floor(self._samples_in_set / self.batch_size))

    def __getitem__(self, key):
        """
        Generating a batch of data
        :returns: a batch of data
        """
        # at first generate the indices:
        indexes = self.indexes[
            key * self.batch_size:(key + 1) * self.batch_size]
        data = [self.data[index] for index in indexes]
        data = tf.convert_to_tensor(data, dtype=tf.float32)
        return data

    def on_epoch_end(self):
        """
        Updates indexes after each epoch, also performs shuffeling
        """
        self.indexes = np.arange(self._samples_in_set)

        # shuffel, if needen, maybe setting it to default:
        if self.shuffle is True:
            np.random.shuffle(self.indexes)
