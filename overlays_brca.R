library(tidyverse)
library(STRINGdb)

background <- read_csv("genericVAE/brca_recons.csv")$"name"

string_db <- STRINGdb$new(version="11.5",
                          species=9606,
                          input_directory="",
                          #backgroundV = background,
                          score_threshold=200
                          )
middle = read.csv("genericVAE/middle_brca.tsv", sep="\t")

middle_mapped <- string_db$map(middle, "names", removeUnmappedRows = T)

# string_db$plot_network(middle_mapped)

# clustering
cluster_list <- string_db$get_clusters(middle_mapped$STRING_id)

par(mfrow=c(2,2))
for(i in seq(1:4)){string_db$plot_network(cluster_list[[i]])}

# check enrichment of these clusters:
enlist <- list()

for(i in seq(1:4)){
  new_enrichment <- string_db$get_enrichment(cluster_list[[i]])
  enlist[[length(enlist) + 1]] <- new_enrichment
}

top = read.csv("genericVAE/top_350_brca.tsv", sep="\t")

top_mapped <- string_db$map(middle, "names", removeUnmappedRows = T)

# string_db$plot_network(middle_mapped)

# clustering
cluster_list <- string_db$get_clusters(top_mapped$STRING_id)

par(mfrow=c(2,2))
for(i in seq(1:4)){string_db$plot_network(cluster_list[[i]])}

# check enrichment of these clusters:
enlist <- list()

for(i in seq(1:4)){
  new_enrichment <- string_db$get_enrichment(cluster_list[[i]])
  enlist[[length(enlist) + 1]] <- new_enrichment
}

bottom = read.csv("genericVAE/end_brca.tsv", sep="\t")

bottom_mapped <- string_db$map(middle, "names", removeUnmappedRows = T)

# string_db$plot_network(middle_mapped)

# clustering
cluster_list <- string_db$get_clusters(bottom_mapped$STRING_id)

par(mfrow=c(2,2))
for(i in seq(1:4)){string_db$plot_network(cluster_list[[i]])}

# check enrichment of these clusters:
enlist <- list()

for(i in seq(1:4)){
  new_enrichment <- string_db$get_enrichment(cluster_list[[i]])
  enlist[[length(enlist) + 1]] <- new_enrichment
}



