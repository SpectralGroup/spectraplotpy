# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 17:55:52 2014

@author: lbressan
"""
import matplotlib.pyplot as plt
import spectraplotpy as spp
    
    
def make_plots():    
    """
    Function that loads two spectra and 
    plots them in the different subplots.
    """
    fig = plt.figure(1)
    ax1 = fig.add_subplot(2, 1, 1)
    filename1 = 'sampledata/01-CD-Aviv62DS/CSA/CSA.CD'
    filename2 = 'sampledata/01-CD-Aviv62DS/CSA/blank.CD'
    imp1 = spp.AvivImporter(filename1)
    sp1 = spp.Spectrum(imp1.dataset)
    imp2 = spp.AvivImporter(filename2)
    sp2 = spp.Spectrum(imp2.dataset)
    spp.plot_spectra(ax1, [sp1, sp2])

    ax2 = fig.add_subplot(2, 1, 2)
    filename1 = 'sampledata/02-CD-Mos500/csa.bka'
    filename2 = 'sampledata/02-CD-Mos500/p07-10tfe.bka'
    imp1 = spp.MosImporter(filename1)
    sp1 = spp.Spectrum(imp1.dataset)
    imp2 = spp.MosImporter(filename2)
    sp2 = spp.Spectrum(imp2.dataset)
    spp.plot_spectra(ax2, [sp1, sp2], '--o', color='g')
    plt.show()


if __name__ == '__main__':
    make_plots()


