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
"""
It plots multiple spectra.
"""
import custom_exceptions as ce
import warnings 
import matplotlib.pyplot as plt
import spectraplotpy as spp
import numpy as np


def plot_spectra(*sp_list,  **kwargs):
    """
    Function that takes a list of spectra in input and plots them
    by calling their spectra plot method.
    """
    axes = kwargs.get('axes', plt.gca())
    for sp in sp_list:
        # here we pass an axes named argument the value of the axes
        # local variable
        sp.plot(axes=axes)

    return axes


def average_spectra(*sp_list, **kwargs):
    """
    Create average spectra from a list of spectra.
    
    Metadata is taken from the first spectrum. Existing y_errors are over-
    written, existing x_errros are not modified.
    
    Parameters
    ----------
    sp_list : Array of Spectrum objects
    
    ddof :  int = 1
        Delta Degrees of fredom. The standard deviation is calcualted as 
        s = sqrt(1/(N - ddof)*Sum(avg(x)-x_i)), where N is the number of elements

    error_type = : {'st_dev', 'st_err'} = 'st_err' 
        The type of error (uncertantiy) returned. 
        'st_dev' is the standard deviation of the sample
        'st_err' is the standard error (st_dev/sqrt(n))
        
    """
    ddof = kwargs.get('ddof', 1)
    error_type = kwargs.get('error_type', 'st_err')
    if not error_type in ('st_dev', 'st_err'):
        raise ValueError("Error_type shuld be either 'st_dev' or 'st_err'and not '" 
                         + error_type + "'!")
    N = len(sp_list);
    if N == 0:
        raise ValueError("sp_list can not be empty!")

    spectrum = sp_list[0].copy()

    if N == 1:
        warnings.warn("Only one spectrum passed to average_spectra().")
        return spectrum

    #Check that all spectra are compatible (ie have same x-values, etc)
    #TODO: Append to exception msg, which two spectra are incompatible   
    for sp in sp_list[1:]:
        spp.check_compatible_x(spectrum, sp)         
        
    #get the mean        
    for sp in sp_list[1:]:
        spectrum.dataset.y += sp.dataset.y
    spectrum.dataset.y /= N

    #get the standard deviation
    st_dev=np.zeros_like(spectrum.dataset.y)    
    for sp in sp_list:
        st_dev += np.square(sp.dataset.y - spectrum.dataset.y)
        
    st_dev /= N - ddof   
    st_dev = np.sqrt(st_dev)
    
    if error_type.lower() == 'st_err':
        st_dev/= np.sqrt(N) # should it be here N - ddof as well?

    spectrum.dataset.y_errors = st_dev

    return spectrum
