# just to get an idea how pandas was used top filter out stuff:
import pandas as pd


data = pd.DataFrame({"Hugo_Symbol": []})
trans_assoc = pd.DataFrame([])
data.loc[data["Hugo_Symbol"].isin(trans_assoc["c(tf_bnd_genes, genes)"])]
