import pandas as pd
import numpy as np
import generic_VAE as gen


data = pd.read_csv("../hnsc-rsem-fpkm-tcga-t.txt", sep="\t")
darry = np.array(data)[:, 2:].astype("float32").T
log_norm = np.log(darry + 1)
log_norm = np.interp(log_norm, (log_norm.min(), log_norm.max()), (1, 0))

vae_build = gen.Builder(log_norm.shape[1], [191], [191], 19)
vae = gen.VAE(vae_build)

vae.compile()
vae.fit(log_norm, epochs=23)
