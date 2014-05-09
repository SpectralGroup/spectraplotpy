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
Created on Wed March 19 2014

@author: ariamania, lbressan
"""

class SpectraPlotPyError(Exception):
    """
    Exception of the SpectraPlotPy library.
    """
    pass


class XCompatibilityError(SpectraPlotPyError):
    """
    Exception of the SpectraPlotPy library: 
    The length of x and y are different!
    """
    pass
