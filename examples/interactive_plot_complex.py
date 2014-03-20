# -*- coding: utf-8 -*-
#
# This file is part of spectraplotpy.
#
# spectraplotpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# spectraplotpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with spectraplotpy.  If not, see <http://www.gnu.org/licenses/>.
#

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


