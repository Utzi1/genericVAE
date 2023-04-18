"""
File: dummmy_training_skript.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: Just a skript to play around with the generic vae model
"""

import tensorflow as tf
import numpy as np
import generic_VAE

# create some random, uniformly distributed tensors:
training_dummys = np.asarray(
        [tf.random.uniform((400,)) for item in range(1000)])

# create some testing tensors:
testing_dummys = np.asarray(
        [tf.random.uniform((400,)) for item in range(500)])

# this is completely senseless, the part where a training-set and one for
# testing was created the VAE is unsupervised (in this case)
dummy_data = np.concatenate((training_dummys, testing_dummys))

dummy_vae = generic_VAE.Builder(
        input_shape=(400, ),
        encoder_shape=[400, 200, 100, 40, 20, 4],
        decoder_shape=[4, 20, 40, 100, 200, 400],
        latent_dims=5,
        dropout_rate=0)

vae = generic_VAE.VAE(dummy_vae)
vae.compile()
vae_hist = vae.fit(dummy_data, epochs=5, batch_size=20)

# acess index of  min and max vals:
recons = vae.feature_reconstruction.numpy()
np.where(recons == recons.min())[0][0]
np.where(recons == recons.max())[0][0]
