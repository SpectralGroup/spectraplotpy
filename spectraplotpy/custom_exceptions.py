# -*- coding: utf-8 -*-
"""
Created on Wed March 19 2014

@author: ariamania, lbressan
"""

class SpectraPlotPyError(Exception):
    """
    Exception of the SpectraPlotPy library.
    """
    pass


class LengthError(SpectraPlotPyError):
    """
    Exception of the SpectraPlotPy library: 
    The length of x and y are different!
    """
    pass
