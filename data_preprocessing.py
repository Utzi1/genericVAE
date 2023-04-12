import h5py
import numpy as np

def log_norm(data=np.array([])):
    return np.log(data.astype("float32") + 1.)

def scale(data):
    return data * (1 / np.max(data))

def scale_by_sample(data):
    return np.apply_along_axis(scale, axis=1, arr=data)

def read_from_h5(file='.', set_name="data"):
    with h5py.File(file) as f:
        data = f.get(set_name)
    return data
