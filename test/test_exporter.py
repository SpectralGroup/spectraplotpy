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
from spectraplotpy import BaseGraphicExporter

from spectraplotpy import Dataset

from mock import Mock, patch

def test_construction():
    """Test the constructor of the class Exporter"""
    assert Exporter([])

def test_txt_construction():
    """Test construction of the class BaseTextExporter"""
    assert BaseTextExporter([])

def test_default_function():
    """Test for basic functionality"""
    dataset = Dataset()
    bte = BaseTextExporter(dataset)
    
    fmock = Mock()
    bte.write(fmock)

    assert fmock.write.assert_called()
    assert bte.text() == str(bte)
    
    assert bte.save('.testfile.txt') is None
    import os.path
    assert os.path.isfile('.testfile.txt')
    os.remove('.testfile.txt')


def test_aviv_exporter():
    """Test for specific functionality of the AvivExporter"""
    
    import os.path

    dataset = Dataset(x=[1, 2, 3], y=[1, 2, 3],
                 metadata={'temp': 10, 'date': 'today'})

    ave = AvivExporter(dataset)

    with open('.testfile.cd', 'w') as fhandler:
        assert ave.write(fhandler) is None

    assert os.path.isfile('.testfile.cd')
    os.remove('.testfile.cd')

    assert ave.save('.testfile.cd') is None
    assert os.path.isfile('.testfile.cd')
    os.remove('.testfile.cd')

    assert ave.text() == str(ave)


def test_csv_construction():
    """Test the construction of the CSVExporter"""
    dataset = Dataset()
    assert CSVExporter(dataset)


def test_csv_exporter():
    """Test for specific functionality of the CSVExporter"""
    
    import os.path

    dataset = Dataset(x=[1, 2, 3], y=[1, 2, 3],
                 metadata={'temp': 10, 'date': 'today'})

    ave = CSVExporter(dataset)

    with open('.testfile.csv', 'w') as fhandler:
        assert ave.write(fhandler) is None

    assert os.path.isfile('.testfile.csv')
    os.remove('.testfile.csv')

    assert ave.save('.testfile.csv') is None
    assert os.path.isfile('.testfile.csv')
    os.remove('.testfile.csv')

    assert ave.text() == str(ave)


def test_csv_exporter_x_errors():
    """Test if the exporter does not stack standalone x errors."""

    dataset = Dataset(x=[1, 2, 3], y=[1, 2, 3], errors_x = -1,
                      metadata={'temp': 10, 'date': 'today'})
    csv_val = CSVExporter(dataset)
    assert not '-1' in csv_val.text()

    dataset = Dataset(x=[1, 2, 3], y=[1, 2, 3], errors_x=[-1, -1, -1],
                      metadata={'temp': 10, 'date': 'today'})
    csv_val = CSVExporter(dataset)
    assert not '-1' in csv_val.text()
