# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 22:36:41 2014

@author: lbressan
"""
"""
It plots multiple spectra.
"""
import  spectraplotpy as spp


def plot_spectra(*sp_list , **kwarg):
    """
    Function that takes a list of spectra in input and plots them
    by calling their spectra plot method.
    """
    for sp in sp_list:
        sp.plot(**kwarg)












