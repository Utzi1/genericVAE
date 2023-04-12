"""
File: reading.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: A few functions to read files without fuzzing around
"""
import h5py
import pandas as pd

def read_from_h5(file='.', set_name="data"):
    """
    Takes the file-path and the set_name (key) to read data from a h5-file

    :file: filepath
    :set_name: name or key specifying the set (from the file)
    :returns: h5 dataset
    """
    with h5py.File(file) as f:
        data = f.get(set_name)
    return data


def read_gct_from_GTEx(file="."):
    """
    Reads from GTEx-gct files (V8)
    :file: filepath
    :returns: pandas dataframe

    """
    return pd.read_csv(file, sep='\t', skiprows=2, index_col=0)
