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
import pytest


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
    ds2 = spp.Dataset(x=[1, 2, 3], y=[1, 3, 5])
    ds3 = spp.Dataset(x=[1, 2, 3], y=[1, 1, 1])    
    mean = [1, 2, 3]    
    
    st_dev = [0, 1, 2]
    st_err = st_dev/np.sqrt(3)
    print st_err
    sp1 = spp.Spectrum(ds1)
    sp2 = spp.Spectrum(ds2)
    sp3 = spp.Spectrum(ds3)

    sp = spp.average_spectra(sp1, sp2, sp3)
    #assert np.array_equal(sp3.dataset.y, ( sp1.dataset.y +  sp2.dataset.y +  sp2.dataset.y)/3)
    assert np.array_equal(sp.dataset.y, mean)    
    #test st dev
    assert np.array_equal(sp.dataset.errors_y, st_err)
    
    sp = spp.average_spectra(sp1, sp2, sp3, error_type='st_dev')
    assert np.array_equal(sp.dataset.y, mean)    
    assert np.array_equal(sp.dataset.errors_y, st_dev)
    
    #TODO: ddof testing...
   
def test_average_spectra_one_spec():   
    ds1 = spp.Dataset(x=[1, 2, 3], y=[1, 2, 3])
    sp1 = spp.Spectrum(ds1)
    sp = spp.average_spectra(sp1)
    assert np.array_equal(sp1.dataset.y, sp.dataset.y)
    
def test_average_spectra_incompatible_x():   
    sp1 = spp.Spectrum(spp.Dataset(x=[1, 2, 3], y=[1, 2, 3]))
    sp2 = spp.Spectrum(spp.Dataset(x=[1, 2, 4], y=[1, 2, 3]))
    
    with pytest.raises(spp.XCompatibilityError) as e:
        sp = spp.average_spectra(sp1, sp2)
    assert e.value[0] == "Not all values of dataset.x are the same!"

def test_average_spectra_incompatible_x_len():   
    sp1 = spp.Spectrum(spp.Dataset(x=[1, 2, 3, 4], y=[1, 2, 3, 4]))
    sp2 = spp.Spectrum(spp.Dataset(x=[1, 2, 4],    y=[1, 2, 3]))
    
    with pytest.raises(spp.XCompatibilityError) as e:
        sp = spp.average_spectra(sp1, sp2)
    assert e.value[0] == "Lengths of dataset.x are not equal! (4 != 3)"    

if __name__ == "__main__":
    test_average_spectra_incompatible_x()