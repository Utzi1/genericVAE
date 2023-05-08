cd genericVAE/
la
ls
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
%save "sliding_window.py"
%save
%save previous_session ~1/
%save previous_session
%hist -f sliding_window.py
ed sliding_window.py
plt.xlabel("Genes ordered by reconstruction error")
plt.ylabel("p-value for TF-enrichment")
plt.plot(plist); plt.show()
middle_part = nlist[1050:1700]
middle_part
tfs = pd.read_csv("evaluation_methods/trrust_rawdata.human.tsv", sep="\t")
tfs
tfs = set(tfs_list["AATF"])
tfs = set(tfs["AATF"])
tfs_in_middle = set(middle_part) & tfs
tfs_in_middle
len(tfs_in_middle
)
%hist -f sliding_window.py
nvim %hist
nvim sliding_window.py
ed sliding_window.py
plt.xlabel("Genes ordered by reconstruction error")
plt.ylabel("p-value for TF-enrichment")
plt.plot(plist); plt.show()
tfs_in_middle = nlist[850:1000]
tfs_in_middle = set(tfs_in_middle) & tfs
tfs_in_middle
plt.xlabel("Genes ordered by reconstruction error")
plt.ylabel("p-value for TF-enrichment")
plt.plot(plist); plt.show()
end = nlist[-300:-1]
end
tfs_end = set(end) & tfs
tfs_end
%hist -f sliding_window.py
