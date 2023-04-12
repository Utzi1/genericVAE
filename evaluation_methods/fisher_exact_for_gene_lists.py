import pandas as pd
from scipy.stats import fisher_exact


def f_exact_test(subset=[], all=[], tfs=[]):
    """Computes a Fisher exact test on gene sets

    :subset: a set of genes, filtered from all genes
    :all: All genes used (for training)
    :tfs: a list of transcription facors, defaulted with data from TRRUST
              version 2
    :returns: TODO
    """
    if len(tfs) == 0:
        tfs = pd.read_csv("trrust_rawdata.human.tsv", sep="\t")

    # make tfs a set:
    tfs = set(tfs["AATF"])
    # the contigency-table
    ctab = [[len(tfs.intersection(subset)),
             len(tfs.difference(subset))],
            [len(subset.difference(tfs)),
             len(all.difference(tfs.union(subset)))]]
    return fisher_exact(ctab)

