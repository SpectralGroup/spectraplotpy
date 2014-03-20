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
