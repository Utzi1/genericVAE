# coding: utf-8
get_ipython().run_line_magic('cd', 'genericVAE/')
la
get_ipython().run_line_magic('ls', '')
import pandas as pd
data = pd.read_csv("recons/GTEx_filtereded_with_genes_in_string.csv")
datd
data
data = pd.read_csv("recons/pancan_recs.csv")
data
data = pd.read_csv("recons/recons_brcarsemfpkmtcgat.csv")
data
nlist = []
window_size=250
for item in range(len(data) -window_size +1)
nlist = data.loc["SRY"]
data
data = pd.read_csv("recons/recons_brcarsemfpkmtcgat.csv", header=False)
data = pd.read_csv("recons/recons_brcarsemfpkmtcgat.csv", header=None)
data
nlist = data.iloc[1]
nlist
nlist = data.iloc[:,1]
nlist
import matplotlib.pyplot as plt
from evaluation_methods.fisher_exact_for_gene_lists import f_exact_test
plist = []

for genes in range(len(nlist) - window_size + 1):
    top = nlist[genes:genes+window_size]
    results = f_exact_test(set(top), set(nlist))
    plist.append(results[0][1])
    
plist
plt.xlabel("Genes ordered by reconstruction error")
plt.ylabel("p-value for TF-enrichment")
plt.plot(plist)
plt.show()
window_size=100
plist = []

for genes in range(len(nlist) - window_size + 1):
    top = nlist[genes:genes+window_size]
    results = f_exact_test(set(top), set(nlist))
    plist.append(results[0][1])
    
plt.xlabel("Genes ordered by reconstruction error")
plt.ylabel("p-value for TF-enrichment")
plt.plot(plist)
plt.show()
window_size=150
plist = []

for genes in range(len(nlist) - window_size + 1):
    top = nlist[genes:genes+window_size]
    results = f_exact_test(set(top), set(nlist))
    plist.append(results[0][1])
    
plt.xlabel("Genes ordered by reconstruction error")
plt.ylabel("p-value for TF-enrichment")
plt.plot(plist); ptl.show()
plt.xlabel("Genes ordered by reconstruction error")
plt.ylabel("p-value for TF-enrichment")
plt.plot(plist); plt.show()
window_size=200
plist = []

for genes in range(len(nlist) - window_size + 1):
    top = nlist[genes:genes+window_size]
    results = f_exact_test(set(top), set(nlist))
    plist.append(results[0][1])
    
plt.xlabel("Genes ordered by reconstruction error")
plt.ylabel("p-value for TF-enrichment")
plt.plot(plist); plt.show()
get_ipython().run_line_magic('save', '"sliding_window.py"')
get_ipython().run_line_magic('save', '')
get_ipython().run_line_magic('save', 'previous_session ~1/')
