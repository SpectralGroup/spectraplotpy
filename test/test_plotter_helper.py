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

@author: lbressan
"""
import spectraplotpy as spp
#import matplotlib.pyplot as plt
from mock import MagicMock

def create_fake_dataset():
    import numpy as np
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
    ds = create_fake_dataset()
    sp = spp.Spectrum(ds)
    sp1 = sp.copy()
    sp2 = sp.copy()

    sp3 = spp.average_spectra(sp, sp1, sp2)

    assert all(sp3.dataset.y == ( sp.dataset.y +  sp1.dataset.y +  sp2.dataset.y)/3)
    
    

