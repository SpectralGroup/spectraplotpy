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
Created on Tue Mar 18 15:53:31 2014

@author: ooscar
"""

#import pytest as pt
import numpy as np

import spectraplotpy as spp

def test_construction():
    """Tests the construction of an empty dataset structure"""
    assert spp.Dataset()
    assert spp.Dataset(x=[1, 2, 3], y=[1, 2, 3])
    
    
def test_length():
    ds = spp.Dataset(x=[1, 2, 3], y=[1, 2, 3]) 
    assert ds.length() == 3
    
    
def test_copy():
    ds = spp.Dataset(x=[1, 2, 3], y=[1, 2, 3]) 
    assert ds.copy()
    
def test_make_numpy_array():
    x = [1, 2, 3]    
    xnp = spp.make_numpy_array(x)    
    assert isinstance(xnp, np.ndarray)
    
def test_make_numpy_array_no_copy():
    x = np.array([1, 2, 3])    
    y = spp.make_numpy_array(x)    
    assert isinstance(y, np.ndarray)    
    
    #check that both x and y are modified
    y[1] = 10
    assert all(x==y)