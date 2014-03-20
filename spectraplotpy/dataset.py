# -*- coding: utf-8 -*-
"""
The Dataset class receives and holds inputs from the importer class and holds
them for further operations by the spectrum and exporter classes.
"""

import copy
import numpy as np

class Dataset():
    """
    DAta structure holding a 2D representation of an spectrum.
    """
    def __init__(
            self,
            x=np.array([]), y=np.array([]),
            metadata={},
            errors_x=None, errors_y=None, 
            units_x=None, units_y=None, 
            dim_x=None, dim_y=None
        ):
        self.x = x
        self.y = y
        self.metadata = metadata
        self.errors_x = errors_x
        self.errors_y = errors_y
        self.units_x = units_x
        self.units_y = units_y
        self.dim_x = dim_x
        self.dim_y = dim_y

    def _validate_data(self):
        """Check that x and y data match"""
        if len(self.x) != len(self.y):
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
            and len(self.x) == len(self.errors_x):
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

    def length(self):
        """
        Returns the len of the dataset assuming that the dataset is valid...
        """
        return len(self.x)

    def copy(self):
        """
        Member deep copy operation        
        """
        return copy.deepcopy(self)
