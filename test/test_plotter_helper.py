# -*- coding: utf-8 -*-
"""
Created on Wed March 19 22:36:41 2014

@author: lbressan
"""
import spectraplotpy as spp
import matplotlib.pyplot as plt
from mock import MagicMock

def create_fake_dataset():
    import numpy as np
    ds = spp.Dataset()
    ds.x = np.array([1,2,3,4])
    ds.y = np.array([2,4,6,8])
    return ds 



def test_plotter_helper():
    mock_fig = plt.figure();
    mock_fig.plot = MagicMock()

    ds = create_fake_dataset()
    sp = spp.Spectrum(ds)
    
    spp.plot_spectra(mock_fig, [sp, sp.copy()])
    
    assert mock_fig.plot.call_count == 2 

    
