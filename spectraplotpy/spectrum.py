""" spectrum.py """

import copy
import matplotlib.pyplot as plt


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
        self.dataset.y -= other.dataset.y
            
            
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
        
        
    def plot(self, *args, **kwargs):
        """
        makes a x-y line plot of the spectrum in place
        """

        plt.plot(self.dataset.x, self.dataset.y, *args, **kwargs)
        
        
    def y_error_plot(self, *args, **kwargs):
        """
        makes a plot of the y symmetric error bars of the spectrum in place
        """
        x_data = self.dataset.x
        y_data = self.dataset.y        
        y_error = self.dataset.error_y
        
        plt.errorbar(x_data, y_data, yerr = y_error, *args, **kwargs)