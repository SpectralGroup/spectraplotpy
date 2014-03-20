# -*- coding: utf-8 -*-

"""
spectrum.py
"""

import copy
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
        the plot function
        """

        if self.dataset.errors_x is not None \
           or self.dataset.errors_y is not None:

            if self.dataset.errors_x is not None:
                if self.dataset.errors_y is not None:
                    return self._plot_xy_error(fig, *args, **kwargs)
                else:
                    return self._plot_x_error(fig, *args, **kwargs)

            else:
                return self._plot_y_error(fig, *args, **kwargs)

        fig.plot(self.dataset.x, self.dataset.y, *args, **kwargs)


    def _plot_xy_error(self, fig, *args, **kwargs):
        """
        Private function that calls the auxiliar `errorbar` method provided
        by the `fig` object and plots the errorbars propertly
        """
        return fig.errorbar(
            self.dataset.x, self.dataset.y,
            self.dataset.errors_x, self.dataset.errors_y,
            *args, **kwargs
        )


    def _plot_x_error(self, fig, *args, **kwargs):
        """
        Private function that calls the auxiliar `errorbar` method provided
        by the `fig` object and plots the errorbars propertly
        """
        return fig.errorbar(
            self.dataset.x, self.dataset.y,
            self.dataset.errors_x,
            *args, **kwargs
        )


    def _plot_y_error(self, fig, *args, **kwargs):
        """
        Private function that calls the auxiliar `errorbar` method provided
        by the `fig` object and plots the errorbars propertly
        """
        return fig.errorbar(
            self.dataset.x, self.dataset.y,
            yerr=self.dataset.errors_y,
            *args, **kwargs
        )
