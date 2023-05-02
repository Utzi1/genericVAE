"""
File: pcc.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: stuff for computation of pearson corelation
"""

import numpy as np
import pandas as pd
from pathlib import Path

base_path = Path(__file__).parent
file_path = (base_path / "trrust_rawdata.human.tsv").resolve()


def tf_extractor(genes, tf_list=[]):
    """TODO: Docstring for tf_extractor.

    :genes: TODO
    :tf_list: TODO
    :returns: TODO

    """
    if len(tf_list) == 0:
        tfs = pd.read_csv(file_path, sep="\t")
        # make tfs a set:
        tf_list = set(tfs["AATF"])

    return set(genes) & set(tf_list)


def pcc_calculator(exp_data, tfs):
    """TODO: Docstring for pcc_.

    Mainly stolen from Julia Åkessons comhub pcc method

    :arg1: TODO
    :returns: TODO

    """
    tfs = [tf for tf in tfs if tf in exp_data.columns]
    tfs_index = np.where(np.isin(exp_data.columns, tfs) == True)[0]  # E: E71
    tfs_new_order = exp_data.columns[tfs_index]
    corrmat = np.corrcoef(np.array(np.array(exp_data.astype("float").T)))
    corrmat = np.abs(corrmat[tfs_index, :])
    corrmat = pd.DataFrame(corrmat, index=tfs_new_order,
                           columns=exp_data.columns)
    net = corrmat.reset_index().melt(id_vars=["index"])
    net.columns = ["TF", "target", "confidence"]
    net = net[net.TF != net.target]
    net_sort = net.sort_values(by="confidence", ascending=False).iloc[:, :]

    return net_sort
