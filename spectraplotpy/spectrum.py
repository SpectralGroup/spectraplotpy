""" spectrum.py """

import copy


class Spectrum(object):    
    """ An object class defining a spectrum """
    def __init__(self, dataset):
        """ """
        self.dataset = dataset
        


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


    def sub(self, dataset):
        """ substracs two spectra in place"""
        pass
    
    
    def copy(self):
        """ creates a copy of a spectrum"""
        return copy.deepcopy(self)
        