library('MOMA')
library('clusterProfiler')
library('org.Hs.eg.db')
library('tidyverse')
library('STRINGdb')

data = read_csv("recons/recons_per_gene.csv") %>% arrange(recon_error)

ref = data$name

top_200 = data$name[1:100]

top_200

ego = enrichGO(gene = top_200,
               OrgDb = org.Hs.eg.db,
               universe = ref,
               keyType = "SYMBOL")

barplot(ego)


string_db = STRINGdb$new(species=9606,
                         score_threshold=200,
                         input_directory="")

top_200 = data.frame("gene"=top_200)

top_200_mapped = string_db$map(top_200, "gene", removeUnmappedRows = T)
string_db$plot_network(top_200)
