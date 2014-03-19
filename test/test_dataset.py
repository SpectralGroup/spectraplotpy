# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 15:53:31 2014

@author: hnjoku
"""

from spectraplotpy import Dataset

def test_construction():
    """Tests the construction of an empty dataset structure"""
    assert Dataset()
    assert Dataset(x=[1, 2, 3], y=[1, 2, 3])


def test_validation():
    """Tests the validation of an empty dataset"""
    ds = Dataset()
    assert ds.validate() == True
