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
A couple of tests for the Exporter class and subclasses
"""

from spectraplotpy import Exporter
from spectraplotpy import BaseTextExporter
from spectraplotpy import CSVExporter
from spectraplotpy import AvivExporter
#from spectraplotpy import GraphicExporter

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




