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
    assert np.array_equal(sp.dataset.y_errors, st_err)
    
    sp = spp.average_spectra(sp1, sp2, sp3, error_type='st_dev')
    assert np.array_equal(sp.dataset.y, mean)    
    assert np.array_equal(sp.dataset.y_errors, st_dev)
    
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

def test_average_spectra_wrong_error_type():   
    sp1 = spp.Spectrum(spp.Dataset(x=[1, 2, 3], y=[1, 2, 3]))
    sp2 = spp.Spectrum(spp.Dataset(x=[1, 2, 3], y=[1, 2, 3]))
    
    with pytest.raises(ValueError) as e:
        sp = spp.average_spectra(sp1, sp2, error_type='standard_something')
    assert e.value[0] == ("Error_type shuld be either 'st_dev' or 'st_err'"
                          "and not 'standard_something'!")



def test_get_poly_baseline():
    """This is a bit of a brittle test, as we compare a fit 
    to a precalculated fit. But probably better than nothing"""
    target_y = np.array([  9.95847828e-01,   9.98809914e-01,   1.00097735e+00,
         1.00236653e+00,   1.00299384e+00,   1.00287565e+00,
         1.00202835e+00,   1.00046833e+00,   9.98211967e-01,
         9.95275652e-01,   9.91675766e-01,   9.87428695e-01,
         9.82550823e-01,   9.77058534e-01,   9.70968212e-01,
         9.64296243e-01,   9.57059010e-01,   9.49272898e-01,
         9.40954291e-01,   9.32119574e-01,   9.22785132e-01,
         9.12967348e-01,   9.02682607e-01,   8.91947295e-01,
         8.80777794e-01,   8.69190490e-01,   8.57201767e-01,
         8.44828009e-01,   8.32085601e-01,   8.18990927e-01,
         8.05560373e-01,   7.91810321e-01,   7.77757158e-01,
         7.63417266e-01,   7.48807031e-01,   7.33942837e-01,
         7.18841069e-01,   7.03518110e-01,   6.87990346e-01,
         6.72274161e-01,   6.56385939e-01,   6.40342064e-01,
         6.24158922e-01,   6.07852897e-01,   5.91440372e-01,
         5.74937733e-01,   5.58361365e-01,   5.41727650e-01,
         5.25052974e-01,   5.08353722e-01,   4.91646278e-01,
         4.74947026e-01,   4.58272350e-01,   4.41638635e-01,
         4.25062267e-01,   4.08559628e-01,   3.92147103e-01,
         3.75841078e-01,   3.59657936e-01,   3.43614061e-01,
         3.27725839e-01,   3.12009654e-01,   2.96481890e-01,
         2.81158931e-01,   2.66057163e-01,   2.51192969e-01,
         2.36582734e-01,   2.22242842e-01,   2.08189679e-01,
         1.94439627e-01,   1.81009073e-01,   1.67914399e-01,
         1.55171991e-01,   1.42798233e-01,   1.30809510e-01,
         1.19222206e-01,   1.08052705e-01,   9.73173925e-02,
         8.70326520e-02,   7.72148683e-02,   6.78804258e-02,
         5.90457091e-02,   5.07271024e-02,   4.29409904e-02,
         3.57037574e-02,   2.90317879e-02,   2.29414663e-02,
         1.74491771e-02,   1.25713047e-02,   8.32423363e-03,
         4.72434828e-03,   1.78803311e-03,  -4.68327427e-04,
        -2.02834889e-03,  -2.87564682e-03,  -2.99383678e-03,
        -2.36653431e-03,  -9.77354971e-04,   1.19008569e-03,
         4.15217213e-03])
    x = range(1,101)
    y = np.random.rand(100)
    y[0:10]  = 1
    y[90:100]= 0
    #generate a dataset and spectrum from this baseline 
    ds = spp.Dataset(x=x, y=y)
    s = spp.Spectrum(ds)    
    indices = np.append(range(0,10), range(90,100))
    baseline = spp.get_poly_baseline(s, indices, deg = 3)   
    
    assert(np.all(baseline.dataset.x == s.dataset.x))
    assert(np.allclose(baseline.dataset.y, target_y))

def test_minmax_norm():
    sp = spp.Spectrum(spp.Dataset(x=[1, 2, 3, 4], y=[-1, 2, 3, -4]))
    spp.minmax_normalize(sp)
    
    assert(np.all(sp.dataset.y == np.array([-1, 2, 3, -4])/4.))
    

if __name__ == "__main__":
    test_average_spectra_incompatible_x()