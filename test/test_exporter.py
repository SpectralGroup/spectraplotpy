# -*- coding: utf-8 -*-

"""
A couple of tests for the Exporter class and subclasses
"""

from spectraplotpy import Exporter
from spectraplotpy import BasePlotExporter
from spectraplotpy import BaseTextExporter
from spectraplotpy import CSVExporter
from spectraplotpy import AvivExporter

from spectraplotpy import Dataset

def test_construction():
    """Test the constructor of the class Exporter"""
    assert Exporter([])

def test_txt_construction():
    """Test construction of the class BaseTextExporter"""
    assert BaseTextExporter([])

def test_default_function():
    """Test for basic functionality"""
    ds = Dataset()
    bte = BaseTextExporter(ds)
    
    with open('.testfile.txt', 'w') as f:
        assert bte.write(f) is None

    assert bte.text()
    assert bte.save('.testfile.txt') is None

def test_aviv_exporter():
    """Test for specific functionality of the AvivExporter"""
    ds = Dataset(x=[1, 2, 3], y=[1, 2, 3],
                 metadata={'temp': 10, 'date': 'today'})
    ave = AvivExporter(ds)
    
    with open('.testfile.cd', 'w') as f:
        assert ave.write(f) is None

    assert ave.text()
    assert ave.save('.testfile.cd') is None


def test_csv_construction():
    ds = Dataset()
    assert CSVExporter(ds)


def test_plot_construction():
    """Test construction of the class BasePlotExporter"""
    assert BasePlotExporter([])


