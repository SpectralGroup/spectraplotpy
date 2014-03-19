"""
It plots multiple spectra.
"""
import  spectraplotpy as spp


def plot_spectra(sp_list, **kwarg):
    """
    Function that takes a list of spectra in input and plots them
    by calling their spectra plot method.
    """
    for sp in sp_list:
        sp.plot(**kwarg)












