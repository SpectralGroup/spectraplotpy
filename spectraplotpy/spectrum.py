""" spectrum.py """

import copy


class Spectrum(object):    
    """ An object class defining a spectrum """
    def __init__(self, dataset):
        """ """
        self.dataset = dataset
        
#    def __str__(self):
#        return 'spectum('self.dataset.metadata.filename))



    def __add__(self, other):
        """ adds two spectra, returns third spectrum """
        copied = self.copy()
        copied.add(other)
        return copied



    def add(self, other):
        """ adds two spectra in place"""
        self.dataset.y += other.dataset.y
        


    
    def __sub__(self, other):
        """ substracs two spectra, returns third spectrum """
        copied = self.copy()
        copied.sub(other)
        return copied


    def sub(self, other):
        """ substracs two spectra in place"""
        self.dataset.y -= other.dataset.y
            
            
            
    def __mul__(self, const):
        """ multiplies a spectrum with number a in place"""
        copied = self.copy()
        copied.mul(const)
        return copied


        
    def mul(self, const):
        """ multiplies a spectrum with a number """
        self.dataset.y = const * self.dataset.y


        
    def __div__(self, const):
        """ divides a spectrum with number a in place"""
        copied = self.copy()
        copied.div(const)
        return copied

       
            
    def div(self, const):
        """ multiplies a spectrum with a number """
        self.dataset.y = self.dataset.y / const
        
    
    
    def copy(self):
        """ creates a copy of a spectrum"""
        return copy.deepcopy(self)
        