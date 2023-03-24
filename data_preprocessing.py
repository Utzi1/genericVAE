import h5py
import numpy as np


data = np.array(h5py.File("filtered_train.h5", "r").get("reads"))


log_norm = np.log(data + 1)

scaled = log_norm / np.max(log_norm)

hf = h5py.File("ln_center_GTEX.h5", "w")
hf.create_dataset("train", data=scaled)

data = np.array(h5py.File("filtered_test.h5", "r").get("reads"))

log_norm = np.log(data + 1)

scaled = log_norm / np.max(log_norm)

hf.create_dataset("test", data=scaled)
hf.close()
