# -*- coding: utf-8 -*-
"""
Created on Wed March 19 22:36:41 2014

@author: lbressan
"""
"""
It plots multiple spectra.
"""


def plot_spectra(fig, sp_list, *args, **kwarg):
    """
    Function that takes a list of spectra in input and plots them
    by calling their spectra plot method.
    """
    for sp in sp_list:
        sp.plot(fig, *args, **kwarg)
