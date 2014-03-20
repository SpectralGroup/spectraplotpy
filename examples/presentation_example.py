# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 22:21:45 2014

@author: amaniada
"""

import spectraplotpy as spp
import matplotlib.pyplot as plt

filename1 = 'sampledata/01-CD-Aviv62DS/CSA/CSA.CD'

imp1 = spp.AvivImporter(filename1)
sp1 = spp.Spectrum(imp1.dataset)
    
sp2 = sp1 * 2

sp_aver = spp.average_spectra([sp1, sp2]) 
   
spp.plot_spectra(plt, [sp1, sp2, sp_aver],)
plt .title("Plotting test spectra")
plt.xlabel("x")
plt.ylabel("y")
plt.legend( ("spectum 1", "spectrum 2", "average spectrum"),loc = 'upper left')
plt.show()

csve = spp.CSVExporter(sp_aver.dataset)
csve.save('csa.csv')