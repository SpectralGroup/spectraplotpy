# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 15:53:31 2014

@author: hnjoku
"""

import copy

class Dataset():
    """
    """
    def __init__(self):
        self.x = None
        self.y = None
        self.metadata = None
        self.errors_x = None
        self.errors_y = None
        self.units_x = None
        self.units_y = None
        self.dim_x = None
        self.dim_y = None


    def copy(self):
        return copy.deepcopy(self)
