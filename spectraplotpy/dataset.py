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

class Dataset():
    """
    DAta structure holding a 2D representation of an spectrum.
    """
    def __init__(
            self,
            x=np.array([]), y=np.array([]),
            metadata={}, name="",
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
