library(GO.db)
library(org.Hs.eg.db)

go_id = "GO:0006355"
tf_bnd_id = "GO:0008134"

allegs = get(go_id, org.Hs.egGO2ALLEGS)
genes = unlist(mget(allegs,org.Hs.egSYMBOL))

allegs = get(tf_bnd_id, org.Hs.egGO2ALLEGS)
tf_bnd_genes = unlist(mget(allegs, org.Hs.egSYMBOL))

all = data_frame(c(tf_bnd_genes, genes))

write_csv(all, "transcription_assoc.csv")

