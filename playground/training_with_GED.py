"""
File: training_with_GED.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: Simple pre processing and training with gene expression data
"""

import pandas as pd
import keras
import tensorflow as tf
import numpy as np
import generic_VAE


dats = pd.read_csv("hnsc-rsem-fpkm-tcga-t.txt", sep="\t")
# get gene id's into rows and make the sample to cols
# also cut away the hugo symbols and entrez gene ids
data = dats.iloc[:, 3:].transpose()
# making it an array should omit the row anc col names
data = np.asarray(data)

# for log-normalisation:
data = np.log(data + 1)

# find min and max:
scale = 1 / (.5*data.max())

layer = tf.keras.layers.Rescaling(scale=scale, offset=-1)
data = layer(data)


dummy_vae = generic_VAE.Builder(
    input_shape=(19132, ),
    encoder_shape=[400, 200, 100, 40, 20, 4],
    decoder_shape=[4, 20, 40, 100, 200, 400],
    latent_dims=2,
    dropout_rate=0)

vae = generic_VAE.VAE(dummy_vae.decoder_model, dummy_vae.encoder_model)
vae.compile(optimizer=keras.optimizers.Adam())
vae.fit(data, epochs=4, batch_size=10)
