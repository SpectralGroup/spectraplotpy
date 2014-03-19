# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 15:53:31 2014

@author: hnjoku
"""

import copy
import numpy as np

class Dataset():
    """
    DAta structure holding a 2D representation of an spectrum.
    """
    def __init__(self):
        self.data_x = None
        self.data_y = None
        self.metadata = {}
        self.errors_x = None
        self.errors_y = None
        self.units_x = None
        self.units_y = None
        self.dim_x = None
        self.dim_y = None

    def _validate_data(self):
        """Check that x and y data match"""
        if (len(self.data_x) != len(self.data_y)):
            return False
        return True

    def _validate_metadata(self):
        """Check that metadata is OK"""
        return True
    
    def _validate_errors(self):
        """Check if errors are arrays or if their sizes match the data sizes"""
        if isinstance(self.errors_x, np.ndarray) \
        and isinstance(self.errors_y, np.ndarray):
            if len(self.errors_x) == len(self.errors_y) \
            and len(self.data_x) == len(self.errors_x):
                return True
            else:
                return False
        
        elif self.errors_x is None or self.errors_y is None:
            if self.errors_x is self.errors_y:
                return True
            else:
                return False
        
        else:
            if type(self.errors_x) == type(self.errors_y):
                return True
        
        return False
    
    def _validate_units(self):
        """Check that units are OK"""
        return True
    
    def _validate_dims(self):
        """Check that dimensions are OK"""
        return True

    def validate(self):
        """Aggregate output of various checks"""
        return self._validate_data() and \
               self._validate_metadata()  and \
               self._validate_errors() and \
               self._validate_units() and \
               self._validate_dims()


    def copy(self):
        """
        Member deep copy operation        
        """
        return copy.deepcopy(self)
