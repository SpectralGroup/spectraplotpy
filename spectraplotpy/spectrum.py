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
spectrum.py
"""

import copy
import numpy as np
import custom_exceptions 
import matplotlib.pyplot as plt


def check_compatible_x(first_spec, other_spec, raise_exception=True):
    """
    Checks if two spectra can be added or subtracted.
    
    The x values must be of the same length and all must have the same value.
    The length of the y values is checked as well (this is a bit redundant)        
    
    Parameters
    ----------
    other_spec: Spectrum
        The other spectrum that is checked for compatibility against first_spec.
    
    raise_exception=True: bool 
        If false exceptions are not raised
    
    Returns
    -------
    True if spectra are compatible, false otherwise.        
    
    Raises
    ------
    custom_exceptions.XCompatibilityError
    """            
    if len(first_spec.dataset.x) != len(other_spec.dataset.x):
        if raise_exception:            
            fmtstr = "Lengths of dataset.x are not equal! ({l1} != {l2})"            
            raise custom_exceptions.XCompatibilityError(
                fmtstr.format(l1=len(first_spec.dataset.x), l2=len(other_spec.dataset.x)))
        return False        
        
    if not np.array_equal(first_spec.dataset.x, other_spec.dataset.x): 
        if raise_exception:            
            fmtstr = "Not all values of dataset.x are the same!"
            raise custom_exceptions.XCompatibilityError(fmtstr)
        return False    
          
    return True   

class Spectrum(object):
    """
    An object class defining a spectrum
    """
    def __init__(self, dataset):
        """ """
        self.dataset = dataset


#    def __str__(self):
#        return 'spectum('self.dataset.metadata.filename))


    def __add__(self, other):
        """
        adds two spectra, returns third spectrum
        """
        copied = self.copy()
        copied.add(other)
        return copied           

    def add(self, other):
        """
        adds two spectra in place
        """
        check_compatible_x(self, other)
        self.dataset.y += other.dataset.y


    def __sub__(self, other):
        """
        substracs two spectra, returns third spectrum
        """
        copied = self.copy()
        copied.sub(other)
        return copied


    def sub(self, other):
        """
        substracs two spectra in place
        """
        check_compatible_x(self, other)
        self.dataset.y -= other.dataset.y
        

    def __rmul__(self, const):
        """
        reverse multiplication of a number with a spectrum
        """
        copied = self.copy()
        copied.mul(const)
        return copied


    def __mul__(self, const):
        """
        multiplies a spectrum with number returns copy
        """
        copied = self.copy()
        copied.mul(const)
        return copied


    def mul(self, const):
        """
        multiplies a spectrum with a number in place
        """
        self.dataset.y = const * self.dataset.y



    def __div__(self, const):
        """
        divides a spectrum with number 
        """
        copied = self.copy()
        copied.div(const)
        return copied


    def div(self, const):
        """
        multiplies a spectrum with a number a in place
        """
        self.dataset.y = self.dataset.y / const


    def copy(self):
        """
        creates a copy of a spectrum
        """
        return copy.deepcopy(self)

    def plot(self, *args, **kwargs):
        """
        Plots into `axes` using its plot method, the x and y come from
        the dataset and any other argument you pass will be forwarded to
        the plot method
        """
        axes = kwargs.get('axes', plt.gca())
        return axes.plot(self.dataset.x, self.dataset.y, *args, **kwargs)

    def errorbar(self, *args, **kwargs):
        """
        Plots into `axes` using its errorbar method, the x and y come from
        the dataset and any other argument you pass will be forwarded to
        the errorbar method

        Example
        =======

        >>> import matplotlib.pyplot as plt
        >>> sp.errorbar(plt, '--o')


        """
        axes = kwargs.get('axes', plt.gca())
        return axes.errorbar(
            self.dataset.x, self.dataset.y,
            self.dataset.errors_y, self.dataset.errors_x,
            *args, **kwargs)

    def smooth(self, window_len=11, window='hanning'):
        """
        Smoothens spectral data using hanning, hamming, bartlett, and blackman
        schemes and returns smooth data
        """
        if self.dataset.y.ndim != 1:
            raise ValueError, "smooth only accepts 1 dimension arrays."

        if self.dataset.y.size < window_len:
            raise ValueError, "Input vector needs to be bigger than window size"

        if window_len < 3:
            return self.dataset.y

        if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
            raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"


        holdspec = np.r_[self.dataset.y[window_len-1:0:-1], self.dataset.y, self.dataset.y[-1:-window_len:-1]]
        #print(len(s))
        if window == 'flat': #moving average
            holdwindow = np.ones(window_len,'d')
        else:
            holdwindow = eval('numpy.'+window+'(window_len)')

        self.dataset.y = np.convolve(holdwindow/holdwindow.sum(), holdspec, mode='valid')
