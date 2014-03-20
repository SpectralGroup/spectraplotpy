# -*- coding: utf-8 -*-

"""
spectrum.py
"""

import copy
import numpy
# pylint: disable=W0401
from custom_exceptions import *


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
        x_data = self.dataset.x
        y_data = self.dataset.y
        x1_data = other.dataset.x
        y1_data = other.dataset.y
        
        if len(y_data) == len(y1_data) and all(x_data == x1_data):
            self.dataset.y += other.dataset.y
        else:
#            print("Array length don't match")
            raise LengthError("Array length don't match")
            
    
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
        x_data = self.dataset.x
        y_data = self.dataset.y
        x1_data = other.dataset.x
        y1_data = other.dataset.y
        
        if len(y_data) == len(y1_data) and all(x_data == x1_data):
            self.dataset.y -= other.dataset.y
        else:
#            print("Array length don't match")
            raise LengthError("Array length don't match")
            
            
            
    def __rmul__(self, const):
        """ 
        reverse multiplication of a number with a spectrum in place 
        """
        copied = self.copy()
        copied.mul(const)
        return copied
        
        
    def __mul__(self, const):
        """ 
        multiplies a spectrum with number a in place
        """
        copied = self.copy()
        copied.mul(const)
        return copied

    
    def mul(self, const):
        """ 
        multiplies a spectrum with a number 
        """
        self.dataset.y = const * self.dataset.y 


        
    def __div__(self, const):
        """ 
        divides a spectrum with number a in place
        """
        copied = self.copy()
        copied.div(const)
        return copied

            
    def div(self, const):
        """ 
        multiplies a spectrum with a number 
        """
        self.dataset.y = self.dataset.y / const
        
    
    def copy(self):
        """ 
        creates a copy of a spectrum
        """
        return copy.deepcopy(self)
        
        
    def plot(self, fig, *args, **kwargs):
        """
        Plots into `fig` using its plot method, the x and y come from
        the dataset and any other argument you pass will be forwarded to
        the plot method
        """

        return fig.plot(self.dataset.x, self.dataset.y, *args, **kwargs)

    def errorbar(self, fig, *args, **kwargs):
        """
        Plots into `fig` using its errorbar method, the x and y come from
        the dataset and any other argument you pass will be forwarded to
        the errorbar method

        Example
        =======

        >>> import matplotlib.pyplot as plt
        >>> sp.errorbar(plt, '--o')


        """

        return fig.errorbar(
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
 

        holdspec = numpy.r_[self.dataset.y[window_len-1:0:-1], self.dataset.y, self.dataset.y[-1:-window_len:-1]]
        #print(len(s))
        if window == 'flat': #moving average
            holdwindow = numpy.ones(window_len,'d')
        else:
            holdwindow = eval('numpy.'+window+'(window_len)')
 
        smoothout = numpy.convolve(holdwindow/holdwindow.sum(), holdspec, mode='valid')
        return smoothout