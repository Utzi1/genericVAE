"""
File: enrich_plot_over_gene_list.py
Author: ULR
Email: b21utzri@student.his.se
Github: Utzi1
Description: A simple plotting method to find enriched regions over a ranked
             list of genes
"""
from evaluation_methods.fisher_exact_for_gene_lists import f_exact_test
import matplotlib.pyplot as plt
import sys

sys.path.append("..")


class Enricher():
    """
    Holds a list of Enrichment of specified genes in a sliding window over
    a list of genes.
    Also returns you a neat plot of them

    :gene_list: the ranked list of genes, if not given defaulted with the
    trrust-tf-list
    :genes: genes of interest (if they might be enriched)
    :window_size: the size of the window to compute enrichment in
    """

    def __init__(self, gene_list, genes=[], window_size=100):
        self.genes = genes
        self.gene_list = gene_list
        self.window_size = window_size
        self.elist = []
        # and compute all the stuff:
        self._run()

    def _run(self):
        """
        Computes enrichment
        :returns: TODO

        """
        if self.genes:
            for genes in range(len(self.gene_list) - self.window_size + 1):
                top = self.gene_list[genes: genes + self.window_size]
                results = f_exact_test(
                    # the genes in the window
                    set(top),
                    # all genes in the list
                    set(self.gene_list),
                    # The genes you want to test enrichment for
                    set(self.genes))
                self.elist.append(results[0][1])
        else:
            for genes in range(len(self.gene_list) - self.window_size + 1):
                top = self.gene_list[genes: genes + self.window_size]
                results = f_exact_test(
                    # the genes in the window
                    set(top),
                    # all genes in the list
                    set(self.gene_list))
                self.elist.append(results[0][1])

    def enr_plot(self,
                 xlab="",
                 ylab="",
                 title=""):
        """Plots the enrichment over the list of genes
        """
        plt.plot(self.elist)
        if xlab:
            plt.xlabel(xlab)
        else:
            plt.xlabel("Genes ordered by reconstruction error")
        if ylab:
            plt.ylabel(ylab)
        else:
            plt.ylabel("p-value for TF-enrichment")
        if title:
            plt.title(title)
        else:
            plt.title("".join(("p-values over a sliding window with size ",
                               str(self.window_size)
                               )
                              )
                      )
        plt.show()
