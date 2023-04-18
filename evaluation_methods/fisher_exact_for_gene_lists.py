"""
File: fisher_exact_for_gene_lists.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: Allows the user to hand two different sets of geses that will be
             fed to scipy stats as contigency table.

             Sliding window-version was removed, needs to be redone
"""

import pandas as pd
from scipy.stats import fisher_exact
from pathlib import Path

base_path = Path(__file__).parent
file_path = (base_path / "trrust_rawdata.human.tsv").resolve()


def f_exact_test(subset, alle, tfs=[]):
    """Computes a Fisher exact test on gene sets

    :subset: a set of genes, filtered from all genes
    :all: All genes used (for training)
    :tfs: a list of transcription facors, defaulted with data from TRRUST
              version 2
    :returns: The output from the fishers exat test and its contingency table
    """
    if len(tfs) == 0:
        tfs = pd.read_csv(file_path, sep="\t")
        # make tfs a set:
        tfs = set(tfs["AATF"])
    # the contigency-table
    ctab = [[len(tfs & subset),
             len(tfs - subset)],
            [len(subset - tfs),
             len(alle - (tfs | subset))]]
    return [fisher_exact(ctab),
            ctab]
