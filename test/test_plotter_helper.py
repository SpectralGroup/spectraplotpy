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

    
    
def make_plots():    
    plt.figure()
    filename1 = 'sampledata/01-CD-Aviv62DS/CSA/CSA.CD'
    filename2 = 'sampledata/01-CD-Aviv62DS/CSA/blank.CD'
    imp1 = spp.AvivImporter(filename1)
    sp1 = spp.Spectrum(imp1.dataset)
    imp2 = spp.AvivImporter(filename2)
    sp2 = spp.Spectrum(imp2.dataset)
    spp.plot_spectra(plt, [sp1, sp2])
    plt.show()

    fig2 = plt.figure(2)
    ax1 = fig2.add_subplot(2,1,2)
    filename1 = 'sampledata/02-CD-Mos500/csa.bka'
    filename2 = 'sampledata/02-CD-Mos500/p07-10tfe.bka'
    imp1 = spp.MosImporter(filename1)
    sp1 = spp.Spectrum(imp1.dataset)
    imp2 = spp.MosImporter(filename2)
    sp2 = spp.Spectrum(imp2.dataset)
    spp.plot_spectra(ax1, [sp1, sp2], '--o',color='g')
    plt.show()
    
    
if __name__ == "__main__":
    """
    Make the figures.
    """
    make_plots()
