"""
File: data_preprocessing.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: A few functions to pre-process data prior to trainig
"""
import numpy as np


def log_norm(data=np.array([])):
    """
    Log-normalises a np.array prior to training.
    """
    return np.log(data.astype("float32") + 1.)


def scale(data=np.array([])):
    """
    Scales all values in an np.array betrween 1-0
    """
    return data * (1 / np.max(data))


def scale_by_sample(data):
    """
    Scales a numpy-array of samples along axis=1 sample-wise
    """
    return np.apply_along_axis(scale, axis=1, arr=data)
