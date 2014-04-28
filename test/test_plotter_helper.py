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
Created on Wed March 19 22:36:41 2014

@author: lbressan, ajasja
"""
import spectraplotpy as spp
#import matplotlib.pyplot as plt
from mock import MagicMock
import numpy as np

def create_fake_dataset():

    ds = spp.Dataset()
    ds.x = np.array([1, 2, 3, 4])
    ds.y = np.array([2, 4, 6, 8])
    return ds



def test_plot_spectra():
    mock_axes = MagicMock()
    mock_axes.plot = MagicMock()

    ds = create_fake_dataset()
    sp = spp.Spectrum(ds)

    spp.plot_spectra(sp, sp.copy(), axes=mock_axes)

    assert mock_axes.plot.call_count == 2

def test_average_spectra():
    ds1 = spp.Dataset(x=[1, 2, 3], y=[1, 2, 3])
    ds2 = spp.Dataset(x=[1, 2, 3], y=[1, 3, 4])
    ds3 = spp.Dataset(x=[1, 2, 3], y=[1, 1, 2])    
    sp1 = spp.Spectrum(ds1)
    sp2 = spp.Spectrum(ds2)
    sp3 = spp.Spectrum(ds3)

    sp3 = spp.average_spectra(sp1, sp2, sp3)

    assert np.array_equal(sp3.dataset.y, ( sp1.dataset.y +  sp2.dataset.y +  sp2.dataset.y)/3)
    
    

