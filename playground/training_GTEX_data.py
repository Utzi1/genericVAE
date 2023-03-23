import h5py
import generic_VAE
import data_handler
import numpy as np


# read the data:
data = h5py.File("../filtered_train.h5").get("reads")
data_train = data_handler.DataGenerator("reads", "../filtered_train.h5", 10)
input_dims = data[0].shape[0]

# build a VAE:
vae_build = generic_VAE.Builder(
        input_dims,
        [10000, 1000, 500],
        [10000, 1000, 500],
        100,
        dropout_rate=.01)

# make it a Model:
vae_model = generic_VAE.VAE(vae_build)

# complile it:
vae_model.compile()

# for the amount of batches:
batch_size = int(np.floor(input_dims / 100))

# vae_model.fit(data, batch_size=batch_size)
vae_model.fit(data_train)
