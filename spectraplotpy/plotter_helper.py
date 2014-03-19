"""
It plots multiple spectra.
"""
import  spectraplotpy as spp


def plot_spectra(sp_list, **kwarg):
    for sp in sp_list:
        sp.plot(**kwarg)












