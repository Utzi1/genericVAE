"""
File: training_EBP_data.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: Training with
             https://gdc.cancer.gov/about-data/publications/PanCan-CellOfOrigin
"""

import h5py
import generic_VAE
import data_handler
import tensorflow as tf
import numpy as np


# read the data:
# data = h5py.File("ln_filtered_GTEX.h5py").get("train")

with h5py.File("../EBPlusPlusAdjustPANCAN.h5") as train:
    data = train["centered_data"][:]

data_train = data_handler.DataGenerator("centered_data",
                                        "../EBPlusPlusAdjustPANCAN.h5",
                                        10)
input_dims = data[0].shape[0]

# for log-normalisation:
# data = np.log(data + 1)

# find min and max:
# scale = 1 / (.5*data.max())

# layer = tf.keras.layers.Rescaling(scale=scale, offset=-1)

# data = layer(data)
# build a VAE:
vae_build = generic_VAE.Builder(
    input_dims,
    [1000],
    [1000],
    50,
    dropout_rate=.0001)

# make it a Model:
vae_model = generic_VAE.VAE(vae_build)

# complile it:
vae_model.compile()

# for the amount of batches:
batches = int(np.floor(input_dims / 100))

vae_model.fit(data_train, epochs=batches,
              workers=64, use_multiprocessing=True)
