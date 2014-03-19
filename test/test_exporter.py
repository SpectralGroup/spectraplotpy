# -*- coding: utf-8 -*-

"""
A couple of tests for the Exporter class and subclasses
"""

from spectraplotpy import Exporter
from spectraplotpy import BasePlotExporter
from spectraplotpy import BaseTextExporter

def test_construction():
    """Test the constructor of the class Exporter"""
    assert Exporter([])


def test_txt_construction():
    """Test construction of the class BaseTextExporter"""
    assert BaseTextExporter([])


def test_plot_construction():
    """Test construction of the class BasePlotExporter"""
    assert BasePlotExporter([])


