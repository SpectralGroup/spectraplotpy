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
The Dataset class receives and holds inputs from the importer class and holds
them for further operations by the spectrum and exporter classes.
"""

import copy
import numpy as np

def make_numpy_array(in_array):
    """
    Ensures the in_array is converted to a `numpy.ndarray`. If the in array 
    is already an numpy.ndarray the same object is returned
    """
    if isinstance(in_array, np.ndarray):
        return in_array
    else:
        return np.array(in_array)
    
class Dataset():
    """
    DAta structure holding a 2D representation of an spectrum.
    """
    def __init__(
            self,
            x=np.array([]), y=np.array([]),
            metadata={}, name="",
            x_errors=None, y_errors=None, 
            x_unit=None, y_unit=None, 
            x_quantity=None, y_quantity=None
        ):
        self.x = make_numpy_array(x) 
        self.y = make_numpy_array(y)
        self.metadata = metadata
        self.x_errors = x_errors
        self.y_errors = y_errors
        self.x_unit = x_unit
        self.y_unit = y_unit
        self.x_quantity = x_quantity
        self.y_quantity = y_quantity
        self.name = name

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
