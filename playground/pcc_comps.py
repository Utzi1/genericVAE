# coding: utf-8
import pandas as pd
exp = pd.read_csv("brca_filtered_for_comhub.tsv", sep="\t")
exp
tfs = pd.read_csv("evaluation_methods/trrust_rawdata.human.tsv", sep="\t")
tfs
tfs = set(tfs["AATF"])
tfs = [tf for tf in tfs if tf in exp.columns]
import numpy as np
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:network_cutoff, :]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort.to_csv('./networks/'+self.network_name+'/pcc_network.tsv', header=None, index=False, sep='\t')
net_sort.to_csv('brca/pcc_network.tsv', header=None, index=False, sep='\t')
net_sort.to_csv('brca_pcc_network.tsv', header=None, index=False, sep='\t')
net_sort
tfs = pd.read_csv("top_350_brca.tsv", sep="\t")
get_ipython().run_line_magic('hist', '')
exp = pd.read_csv("brca_filtered_for_comhub.tsv", sep="\t")
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort.to_csv('brca_pcc_network.tsv', header=None, index=False, sep='\t')
net_sort
tfs
tfs = pd.read_csv("top_350_brca.tsv", sep="\t")
tfs
tfs = set(tfs["name"])
tfs = set(tfs["names"])
exp = pd.read_csv("brca_filtered_for_comhub.tsv", sep="\t")
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort.to_csv('brca_pcc_network.tsv', header=None, index=False, sep='\t')
net_sort
tfs = pd.read_csv("hubs.tsv", sep="\t")
tfs
tfs = pd.read_csv("hubs.tsv", sep="\t", header=None)
tfs
tfs[0]
tfs = tfs[0]
tfs = set(tfs[0])
tfs
tfs = pd.read_csv("hubs.tsv", sep="\t", header=None)
exp = pd.read_csv("brca_filtered_for_comhub.tsv", sep="\t")
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort.to_csv('brca_pcc_network.tsv', header=None, index=False, sep='\t')
net_sort
tfs = tfs[0]
tfs
tfs = pd.read_csv("hubs.tsv", sep="\t", header=None)
tfs = tfs[0]
exp = pd.read_csv("brca_filtered_for_comhub.tsv", sep="\t")
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort.to_csv('brca_pcc_network.tsv', header=None, index=False, sep='\t')
net_sort
exp = pd.read_csv("brca_filtered_for_comhub.tsv", sep="\t")

tfs = pd.read_csv("evaluation_methods/trrust_rawdata.human.tsv", sep="\t")
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]tfs

tfs = set(tfs["AATF"])
tfs = [tf for tf in tfs if tf in exp.columns]

tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort
exp = pd.read_csv("brca_filtered_for_comhub.tsv", sep="\t")
tfs = pd.read_csv("evaluation_methods/trrust_rawdata.human.tsv", sep="\t")
tfs = set(tfs["AATF"])
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort
get_ipython().run_line_magic('hist', '')
tfs
len(tfs)
trrust_tfs = tfs
tfs = pd.read_csv("top_350_brca.tsv", sep="\t")
tfs
tfs = set(tfs["names"])
tfs & trrust_tfs
tfs & set(trrust_tfs)
tfs = tfs & set(trrust_tfs)
exp = pd.read_csv("brca_filtered_for_comhub.tsv", sep="\t")
tfs = pd.read_csv("evaluation_methods/trrust_rawdata.human.tsv", sep="\t")
tfs = set(tfs["AATF"])
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort
get_ipython().run_line_magic('hist', '')
tfs = pd.read_csv("top_350_brca.tsv", sep="\t")
tfs
tfs = set(tfs["names"])
tfs & trrust_tfs
tfs & set(trrust_tfs)
tfs = tfs & set(trrust_tfs)
tfs = pd.read_csv("top_350_brca.tsv", sep="\t")
tfs
tfs = set(tfs["names"])
tfs = tfs & set(trrust_tfs)
exp
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort
tfs = pd.read_csv("top_350_brca.tsv", sep="\t")
tfs.iloc[:, 0:100]
tfs = set(tfs["names"])
tfs
tfs = tfs & set(trrust_tfs)
tfs
tfs = pd.read_csv("top_350_brca.tsv", sep="\t")
tfs.iloc[:, 0:100]
tfs = pd.read_csv("top_350_brca.tsv", sep="\t")
tfs.iloc[0:100]
tfs = pd.read_csv("top_350_brca.tsv", sep="\t")
tfs.iloc[0:100, 1]
tfs = pd.read_csv("top_350_brca.tsv", sep="\t")
tfs = tfs.iloc[0:100, 1]
tfs = tfs & set(trrust_tfs)
tfs = set(tfs) & set(trrust_tfs)
tfs
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort
import h5py
file = h5py.File("/home/test/Master/Master_Project_2023/data/ln_center_GTEX.h5")
file.keys
file.keys()
file = h5py.File("data/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.h5")
file.keys()
data = pd.DataFrame(file["data])
data = pd.DataFrame(file["data"])
data
file.get(data)
file.get("data")
data = pd.DataFrame(file.get("data"))
data
data = pd.read_hdf("data/GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.h5", key = "data")
data
data = data.drop(data[data.iloc[:, 2:].sum(axis=1) < 35425].index)
print(data.shape)
in_string = pd.read_csv("h_S_string.txt", sep="\t")["preferred_name"]
# filter the frame
fdat = data.loc[data["Description"].isin(in_string)]
fdat
data
data.transpose()
data.index = data["Description"]
data
data.iloc[1:,:]
data.iloc[:,1:]
data = data.iloc[:,1:]
data = data.transpose()
data
data.index=None
data.index
data.index = None
tfs = pd.read_csv("recons/GTEx_filtereded_with_genes_in_string.csv")
tfs
tfs = tfs.iloc[0:100, 1]
tfs
tfs = tfs & set(trrust_tfs)
tfs = set(tfs) & set(trrust_tfs)
tfs
fdat
fdat.index = fdat["Description"]
get_ipython().run_line_magic('ls', '')
fdat
fdat = fdat.transpose()
fdat
fdat.iloc[:,1:]
fdat.iloc[1:,:]
fdat=fdat.iloc[1:,:]
get_ipython().run_line_magic('hist', '')
exp = fdat
[tf for tf in tfs if tf in exp.columns]
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(exp.T))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort
np.corrcoef(np.array(exp.T))
exp = pd.read_csv("brca_filtered_for_comhub.tsv", sep="\t")
exp
fdat
fdat.index.name = None
fdar
fdat
fdat.index.name
np.array(fdat.astype("float"))
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(np.array(exp.astype("float").T)))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort
tfs = pd.read_csv("recons/GTEx_filtereded_with_genes_in_string.csv")
tfs
tfs = tfs.iloc[0:200, 1]
tfs = set(tfs) & set(trrust_tfs)
tfs
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(np.array(exp.astype("float").T)))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort
tfs = tfs.iloc[0:300, 1]
tfs = pd.read_csv("recons/GTEx_filtereded_with_genes_in_string.csv")
tfs = tfs.iloc[0:300, 1]
tfs = set(tfs) & set(trrust_tfs)
tfs
tfs = [tf for tf in tfs if tf in exp.columns]
tfs_index = np.where(np.isin(exp.columns, tfs) == True)[0]
tfs_new_order = exp.columns[tfs_index]
corrmat = np.corrcoef(np.array(np.array(exp.astype("float").T)))
corrmat = np.abs(corrmat[tfs_index, :])
corrmat = pd.DataFrame(corrmat, index=tfs_new_order, columns=exp.columns)
net = corrmat.reset_index().melt(id_vars=['index'])
net.columns = ['TF', 'target', 'confidence']
net = net[net.TF != net.target]
net_sort = net.sort_values(by='confidence', ascending=False).iloc[:, :]
net_sort
len(tfs)
net_sort.iloc[:100000,]
net_sort["confidence"].mean()
net_sort["confidence"].median()
import matplotlib.pyplot as plt
count, bins = np.histogram(net_sort["confidence"])
plt.stairs(count, bins)
plt.show()
count, bins = np.histogram(net_sort["confidence"], bins=100)
plt.stairs(count, bins)
plt.show()
count, bins = np.histogram(net_sort["confidence"], bins=10000)
plt.stairs(count, bins)
plt.show()
plt.stairs(count, bins)
plt.xlabel("Confidence")
plt.ylabel("Count")
plt.show
plt.show()
get_ipython().system('%history "pcc_comps.py"')
