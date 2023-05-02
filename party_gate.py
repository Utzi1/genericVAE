from evaluation_methods.pcc import *

data = pd.read_hdf("data/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.h5", key = "data")

in_string = pd.read_csv("h_S_string.txt", sep="\t")["preferred_name"]

fdat = data.loc[data["Description"].isin(in_string)]
tdat = fdat.transpose()
tdat.reset_index(inplace=True)
tdat.index.name=None
tdat.columns.name=None
tdat.drop("index", axis=1, inplace=True)
tdat.columns = fdat["Description"]
tdat.columns.name=None
tdat.drop(0, inplace=True)

recs = pd.read_csv("recons/GTEx_filtereded_with_genes_in_string.csv")

tops = recs["x"][0:500]

tfs = tf_extractor(tops)

pcc_calculator(tdat, tfs)

recons = pd.read_csv("/home/test/var_b_size_recons_shape_diffs.csv")
recons.sort_values("200recon _recon 10recon _recon 1000", inplace=True)

recs = recons["0"]
eins = recs.iloc[0:4446]
zwei = recs.iloc[4446:2*4446]
drei = recs.iloc[2*4446:3*4446]
vier = recs.iloc[3*4446:]
pcc_calculator(tdat, tf_extractor(eins))

first = pcc_calculator(tdat, tf_extractor(eins))
second = pcc_calculator(tdat, tf_extractor(zwei))
third = pcc_calculator(tdat, tf_extractor(drei))
fourth = pcc_calculator(tdat, tf_extractor(vier))
fourth["confidence"].mean()
third["confidence"].mean()
second["confidence"].mean()
first["confidence"].mean()

import matplotlib.pyplot as plt

count, bins = np.histogram(first["confidence"].fillna(0), bins=500)
plt.stairs(count, bins, label="eins")
count, bins = np.histogram(second["confidence"].fillna(0), bins=500)
plt.stairs(count, bins, label="zwei")
count, bins = np.histogram(third["confidence"].fillna(0), bins=500)
plt.stairs(count, bins, label="drei")
count, bins = np.histogram(fourth["confidence"].fillna(0), bins=500)
plt.stairs(count, bins, label="vier")
plt.legend()
plt.show()
